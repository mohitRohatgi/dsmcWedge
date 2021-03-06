# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:46:14 2015

@author: mohit
"""

import unittest
import numpy as np
import dsmc.dsmc.particles as dm_p
import dsmc.dsmc.movement as dm_r
import dsmc.dsmc.geometry as dm_g
from dsmc.dsmc.reflection_models import Specular


class TestMovementManager(unittest.TestCase):
    def test_convex_horizontal_line1(self):
        particles = dm_p.Particles(100)
        surf = [((1.0, 2.0), (4.0, 2.0))]
        surface = dm_g.SurfaceGroup()
        surface.add_new_group(surf, (0.0, 0.5))
        x = np.linspace(1.0, 2.0, 100)
        particles.x = np.linspace(1.0, 2.0, 100)
        particles.y = np.ones(100, dtype=float) * 4.0
        particles.u = np.zeros(100, dtype=float)
        particles.v = np.ones(100, dtype=float) * -2.0
        movement_manager = dm_r.MovementManager(particles, surface, Specular)
        movement_manager.move_all(2.0)
        for index in range(100):
            self.assertAlmostEqual(particles.x[index], x[index], 4)
            self.assertAlmostEqual(particles.y[index], 4.0, 4)
            self.assertAlmostEqual(particles.u[index], 0.0, 4)
            self.assertAlmostEqual(particles.v[index], 2.0, 4)
    
    
    def test_convex_horizontal_line2(self):
        particles = dm_p.Particles(100)
        surf = [((1.0, 2.0), (4.0, 2.0))]
        surface = dm_g.SurfaceGroup()
        surface.add_new_group(surf, (0.0, 2.5))
        x = np.linspace(1.0, 4.0, 100)
        particles.x = np.linspace(1.0, 4.0, 100)
        particles.y = np.ones(100, dtype=float) * -2.0
        particles.u = np.zeros(100, dtype=float)
        particles.v = np.ones(100, dtype=float) * 2.0
        movement_manager = dm_r.MovementManager(particles, surface, Specular)
        movement_manager.move_all(4.0)
        for index in range(100):
            self.assertAlmostEqual(particles.x[index], x[index], 4)
            self.assertAlmostEqual(particles.y[index], -2.0, 4)
            self.assertAlmostEqual(particles.u[index], 0.0, 4)
            self.assertAlmostEqual(particles.v[index], -2.0, 4)
    
    
    def test_convex_vertical_line(self):
        particles = dm_p.Particles(100)
        surf = [((2.0, 1.0), (2.0, 4.0))]
        surface = dm_g.SurfaceGroup()
        surface.add_new_group(surf, (3.0, 1.5))
        y = np.linspace(1.0, 2.0, 100)
        particles.x = np.ones(100, dtype=float) * 4.0
        particles.y = np.linspace(1.0, 2.0, 100)
        particles.u = np.ones(100, dtype=float) * -2.0
        particles.v = np.zeros(100, dtype=float)
        movement_manager = dm_r.MovementManager(particles, surface, Specular)
        movement_manager.move_all(2.0)
        for index in range(100):
            self.assertAlmostEqual(particles.x[index], 4.0, 4)
            self.assertAlmostEqual(particles.y[index], y[index], 4)
            self.assertAlmostEqual(particles.v[index], 0.0, 4)
            self.assertAlmostEqual(particles.u[index], 2.0, 4)
    
    
    def test_convex_vertical_line1(self):
        particles = dm_p.Particles(100)
        surf = [((2.0, 1.0), (2.0, 4.0))]
        surface = dm_g.SurfaceGroup()
        surface.add_new_group(surf, (1.0, 1.5))
        y = np.linspace(1.0, 4.0, 100)
        particles.x = np.ones(100, dtype=float) * -2.0
        particles.y = np.linspace(1.0, 4.0, 100)
        particles.u = np.ones(100, dtype=float) * 2.0
        particles.v = np.zeros(100, dtype=float)
        movement_manager = dm_r.MovementManager(particles, surface, Specular)
        movement_manager.move_all(4.0)
        for index in range(100):
            self.assertAlmostEqual(particles.x[index], -2.0, 4)
            self.assertAlmostEqual(particles.y[index], y[index], 4)
            self.assertAlmostEqual(particles.v[index], 0.0, 4)
            self.assertAlmostEqual(particles.u[index], -2.0, 4)
    
    
    def test_convex_45_inclined_line(self):
        particles = dm_p.Particles(100)
        surf = [((-2.0, 0.0), (3.0, 5.0))]
        surface = dm_g.SurfaceGroup()
        surface.add_new_group(surf, (0.0, 0.0))
        x = np.linspace(-1.0, 4.0, 100)
        particles.x = np.linspace(-1.0, 4.0, 100)
        particles.y = np.linspace(-1.0, 4.0, 100)
        particles.u = np.ones(100, dtype=float) * -1.0
        particles.v = np.ones(100, dtype=float)
        movement_manager = dm_r.MovementManager(particles, surface, Specular)
        movement_manager.move_all(2.0)
        for index in range(100):
            self.assertAlmostEqual(particles.x[index], x[index], 4)
            self.assertAlmostEqual(particles.y[index], x[index], 4)
            self.assertAlmostEqual(particles.u[index], 1.0, 4)
            self.assertAlmostEqual(particles.v[index], -1.0, 4)
    
    
    def test_concave_hor_ver_line1(self):
        particles = dm_p.Particles(100)
        surf = [((-1.0, 2.0), (-1.0, -3.0)), ((-1.0, -3.0), (4.0, -3.0))]
        surface = dm_g.SurfaceGroup()
        surface.add_new_group(surf, (0.0, 0.0))
        y = np.linspace(0.0, 4.0, 100)
        
        particles.y = np.linspace(0.0, 4.0, 100)
        particles.x = np.ones(100, dtype=float) * 1.0
        particles.u = np.ones(100, dtype=float) * -1.0
        particles.v = np.ones(100, dtype=float) * -1.0
        
        movement_manager = dm_r.MovementManager(particles, surface, Specular)
        movement_manager.move_all(8.0)
        
        for index in range(100):
            self.assertAlmostEqual(particles.u[index], 1.0, 6)
            self.assertAlmostEqual(particles.v[index], 1.0, 6)
            self.assertAlmostEqual(particles.x[index], 5.0, 6)
            self.assertAlmostEqual(particles.y[index], 2.0 - y[index], 6)
    
    
    def test_concave_hor_ver_line2(self):
        particles = dm_p.Particles(100)
        surf = [((-1.0, 2.0), (-1.0, -3.0)), ((-1.0, -3.0), (4.0, -3.0))]
        surface = dm_g.SurfaceGroup()
        surface.add_new_group(surf, (0.0, 0.0))
        y = np.linspace(0.0, 4.0, 100)
        
        particles.y = np.linspace(0.0, 4.0, 100)
        particles.x = np.ones(100, dtype=float) * 1.0
        particles.u = np.ones(100, dtype=float) * -1.0
        particles.v = np.ones(100, dtype=float) * -1.0
        
        movement_manager = dm_r.MovementManager(particles, surface, Specular)
        movement_manager.move_all(8.0)
        
        
        
        for index in range(100):
            self.assertAlmostEqual(particles.x[index], 5.0, 6)
            self.assertAlmostEqual(particles.y[index], 2.0 - y[index], 6)
            self.assertAlmostEqual(particles.u[index], 1.0, 6)
            self.assertAlmostEqual(particles.v[index], 1.0, 6)
    
    
    def test_concave_hor_ver_line3(self):
        particles = dm_p.Particles(100)
        surf = [((-1.0, 2.0), (-1.0, -3.0)), ((-1.0, -3.0), (4.0, -3.0))]
        surface = dm_g.SurfaceGroup()
        surface.add_new_group(surf, (0.0, 0.0))
        y = np.linspace(0.0, 2.0, 100)
        
        particles.y = np.linspace(0.0, 2.0, 100)
        particles.x = np.ones(100, dtype=float) * -0.999999999999999
        particles.u = np.ones(100, dtype=float) * -1.0
        particles.v = np.ones(100, dtype=float) * -1.0
        
        movement_manager = dm_r.MovementManager(particles, surface, Specular)
        movement_manager.move_all(8.0)
        
        for index in range(100):
            self.assertAlmostEqual(particles.x[index], 7.0, 6)
            self.assertAlmostEqual(particles.y[index], 2.0 - y[index], 6)
            self.assertAlmostEqual(particles.u[index], 1.0, 6)
            self.assertAlmostEqual(particles.v[index], 1.0, 6)
    
    
    def test_concave_corner(self):
        particles = dm_p.Particles(100)
        surf = [((-1.0, 2.0), (-1.0, -3.0)), ((-1.0, -3.0), (4.0, -3.0)),
                   ((4.0, -3.0), (4.0, 2.0))]
        surface = dm_g.SurfaceGroup()
        surface.add_new_group(surf, (0.0, 0.5))
        pass



if __name__ == '__main__':
    unittest.main()