#!/usr/bin/env python3
"""Render a realistic 33 cl drink can from a flat label image (Blender bpy, Cycles CPU).

Usage (needs `pip install bpy`, Python version matching the bpy wheel):
  python3 scripts/render_can.py --label label.png --out can.png [--size 720x1280] [--samples 64] [--droplets 280]

The label image is the unwrapped cylinder: width / height ≈ 2.09 (e.g. 2400x1146), front face centred.
Output: transparent PNG of the upright can facing the camera. Present results as 3D renders, not photos.
See references/scroll-cinematography.md §5.
"""
import argparse, math, random

import bpy, bmesh
from mathutils import Vector

PROFILE = [(0, .06), (.62, .03), (.80, 0), (.88, .03), (.95, .15), (.995, .32), (1, .4),
           (1, 3.0), (.99, 3.07), (.93, 3.2), (.86, 3.33), (.845, 3.4), (.86, 3.455), (.84, 3.475),
           (.81, 3.44), (.80, 3.38), (.6, 3.37), (0, 3.37)]
Z0, Z1 = 0.42, 2.98  # label band on the body


def P(node, name, val):
    if name in node.inputs:
        node.inputs[name].default_value = val


def new_mat(name):
    m = bpy.data.materials.new(name); m.use_nodes = True
    return m, m.node_tree, m.node_tree.nodes['Principled BSDF']


def look_at(o, target):
    o.rotation_euler = (Vector(target) - o.location).to_track_quat('-Z', 'Y').to_euler()


def scene_setup():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    s = bpy.context.scene
    s.render.engine = 'CYCLES'; s.cycles.device = 'CPU'; s.cycles.use_denoising = True
    s.render.film_transparent = True
    s.view_settings.view_transform = 'Standard'; s.view_settings.exposure = -.75
    w = bpy.data.worlds.new('W'); s.world = w; w.use_nodes = True
    bg = w.node_tree.nodes['Background']; bg.inputs[0].default_value = (.6, .55, .5, 1); bg.inputs[1].default_value = .2
    def light(name, loc, size, energy, sy=None, color=(1, 1, 1)):
        l = bpy.data.lights.new(name, 'AREA'); l.shape = 'RECTANGLE'; l.size = size; l.energy = energy; l.color = color
        if sy: l.size_y = sy
        o = bpy.data.objects.new(name, l); s.collection.objects.link(o); o.location = loc; look_at(o, (0, 0, 1.8))
    light('key', (-4, -4, 3), 2.5, 650, 6, (1, .95, .88))
    light('rimR', (4.5, 1.5, 2), .6, 700, 7, (1, .9, .8))
    light('rimL', (-4.5, 2, 2), .6, 500, 7, (.9, .95, 1))
    light('strip', (-2.2, -6, 1.8), .25, 260, 6)
    light('top', (0, 0, 7), 4, 350)
    light('fill', (3, -5, 1.5), 3, 160)
    return s


def can_material(label_path):
    m, nt, b = new_mat('can'); N, L = nt.nodes, nt.links.new
    tc = N.new('ShaderNodeTexCoord'); sep = N.new('ShaderNodeSeparateXYZ'); L(tc.outputs['Object'], sep.inputs[0])
    at = N.new('ShaderNodeMath'); at.operation = 'ARCTAN2'; L(sep.outputs[1], at.inputs[0]); L(sep.outputs[0], at.inputs[1])
    u = N.new('ShaderNodeMath'); u.operation = 'MULTIPLY_ADD'; L(at.outputs[0], u.inputs[0]); u.inputs[1].default_value = 1 / (2 * math.pi); u.inputs[2].default_value = .5
    v = N.new('ShaderNodeMath'); v.operation = 'MULTIPLY_ADD'; L(sep.outputs[2], v.inputs[0]); v.inputs[1].default_value = 1 / (Z1 - Z0); v.inputs[2].default_value = -Z0 / (Z1 - Z0)
    uv = N.new('ShaderNodeCombineXYZ'); L(u.outputs[0], uv.inputs[0]); L(v.outputs[0], uv.inputs[1])
    img = N.new('ShaderNodeTexImage'); img.image = bpy.data.images.load(label_path); img.extension = 'EXTEND'; L(uv.outputs[0], img.inputs[0])
    lo = N.new('ShaderNodeMath'); lo.operation = 'GREATER_THAN'; L(v.outputs[0], lo.inputs[0]); lo.inputs[1].default_value = 0
    hi = N.new('ShaderNodeMath'); hi.operation = 'LESS_THAN'; L(v.outputs[0], hi.inputs[0]); hi.inputs[1].default_value = 1
    mask = N.new('ShaderNodeMath'); mask.operation = 'MULTIPLY'; L(lo.outputs[0], mask.inputs[0]); L(hi.outputs[0], mask.inputs[1])
    L(img.outputs['Color'], b.inputs['Base Color'])
    P(b, 'Metallic', .15); P(b, 'Roughness', .32); P(b, 'Coat Weight', .3); P(b, 'Coat Roughness', .05); P(b, 'Specular IOR Level', .35)
    nz = N.new('ShaderNodeTexNoise'); nz.inputs['Scale'].default_value = 140
    bump = N.new('ShaderNodeBump'); bump.inputs['Strength'].default_value = .035; L(nz.outputs['Fac'], bump.inputs['Height']); L(bump.outputs['Normal'], b.inputs['Normal'])
    al = N.new('ShaderNodeBsdfPrincipled'); al.inputs['Base Color'].default_value = (.82, .84, .86, 1); P(al, 'Metallic', 1); P(al, 'Roughness', .2)
    mix = N.new('ShaderNodeMixShader'); L(mask.outputs[0], mix.inputs[0]); L(al.outputs[0], mix.inputs[1]); L(b.outputs[0], mix.inputs[2])
    L(mix.outputs[0], N['Material Output'].inputs['Surface'])
    return m


def make_can(label_path, droplets, seed):
    me = bpy.data.meshes.new('can'); bm = bmesh.new(); seg = 128; rings = []
    for i in range(seg):
        a = 2 * math.pi * i / seg
        rings.append([bm.verts.new((r * math.cos(a), r * math.sin(a), z)) for r, z in PROFILE])
    for i in range(seg):
        A, B = rings[i], rings[(i + 1) % seg]
        for j in range(len(PROFILE) - 1):
            bm.faces.new((A[j], B[j], B[j + 1], A[j + 1]))
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-5); bm.to_mesh(me); bm.free()
    for p in me.polygons: p.use_smooth = True
    can = bpy.data.objects.new('can', me); bpy.context.collection.objects.link(can); me.materials.append(can_material(label_path))
    tm, _, tb = new_mat('tab'); tb.inputs['Base Color'].default_value = (.75, .77, .8, 1); P(tb, 'Metallic', 1); P(tb, 'Roughness', .25)
    bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=.2, depth=.02, location=(-.35, 0, 3.395))
    t = bpy.context.object; t.scale = (1.4, .85, 1); t.data.materials.append(tm); t.parent = can
    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=.06, depth=.03, location=(0, 0, 3.39))
    bpy.context.object.data.materials.append(tm); bpy.context.object.parent = can
    if droplets:
        wm, _, wb = new_mat('water'); P(wb, 'Transmission Weight', 1); P(wb, 'Roughness', 0); P(wb, 'IOR', 1.33)
        bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, radius=1)
        base = bpy.context.object; base.data.materials.append(wm)
        for p in base.data.polygons: p.use_smooth = True
        dm = base.data; bpy.data.objects.remove(base); random.seed(seed)
        for _ in range(droplets):
            a = max(-1.15, min(1.15, random.gauss(0, .65)))  # concentrated on the camera-facing side (+X)
            z = random.uniform(Z0 - .1, Z1 + .05)
            r = random.choice([.012, .018, .024, .03, .04, .055]) * random.uniform(.7, 1.2)
            d = bpy.data.objects.new('drop', dm); bpy.context.collection.objects.link(d)
            d.location = (math.cos(a) * (1 + r * .25), math.sin(a) * (1 + r * .25), z)
            d.rotation_euler = (0, math.pi / 2, a); d.scale = (r * .45, r, r * (1.3 if r > .025 else 1)); d.parent = can
    can.rotation_euler = (0, 0, math.radians(-90))  # label front (+X) faces the camera (-Y)
    return can


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--label', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--size', default='720x1280'); ap.add_argument('--samples', type=int, default=64)
    ap.add_argument('--droplets', type=int, default=280); ap.add_argument('--seed', type=int, default=3)
    a = ap.parse_args()
    w, h = (int(x) for x in a.size.lower().split('x'))
    s = scene_setup(); make_can(a.label, a.droplets, a.seed)
    cam = bpy.data.objects.new('cam', bpy.data.cameras.new('cam')); cam.data.lens = 78
    s.collection.objects.link(cam); cam.location = (0, -11.5, 2.6); look_at(cam, (0, 0, 1.72)); s.camera = cam
    s.render.resolution_x, s.render.resolution_y, s.render.resolution_percentage = w, h, 100
    s.cycles.samples = a.samples; s.render.image_settings.file_format = 'PNG'; s.render.image_settings.color_mode = 'RGBA'
    s.render.filepath = a.out; bpy.ops.render.render(write_still=True)


if __name__ == '__main__':
    main()
