# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2021, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

import unittest

import torch

import nupic.research.frameworks.dendrites.functional as F
from nupic.research.frameworks.dendrites import (
    DendriticAbsoluteMaxGate,
    DendriticAbsoluteMaxGate2d,
    DendriticBias,
    DendriticGate,
    DendriticGate2d,
)


class ApplyDendritesModulesTest(unittest.TestCase):

    def setUp(self):
        batch_size = 5
        num_units = 4
        num_segments = 10
        channels = 3  # 2d versions will use channels x num_units x num_units

        self.y = torch.rand(batch_size, num_units)
        self.dendrite_activations = torch.rand(batch_size, num_units, num_segments)

        self.y_2d = torch.rand(batch_size, channels, num_units, num_units)
        self.dendrite_activations_2d = torch.rand(batch_size, channels, num_units)

    def test_dendritic_bias(self):
        """
        Ensure `dendritic_bias` and `DendriticBias` yield the same outputs.
        """
        module = DendriticBias()
        output_a = F.dendritic_bias(self.y, self.dendrite_activations)
        output_b = module(self.y, self.dendrite_activations)
        all_equal = (output_a[0] == output_b[0]).all()
        self.assertTrue(all_equal)

    def test_dendritic_gate(self):
        """
        Ensure `dendritic_gate` and `DendriticGate` yield the same outputs.
        """
        module = DendriticGate()
        output_a = F.dendritic_gate(self.y, self.dendrite_activations)
        output_b = module(self.y, self.dendrite_activations)
        all_equal = (output_a[0] == output_b[0]).all()
        self.assertTrue(all_equal)

    def test_dendritic_absolute_max_gate(self):
        """
        Ensure `dendritic_absolute_max_gate` and `DendriticAbsoluteMaxGate` yield the
        same outputs.
        """
        module = DendriticAbsoluteMaxGate()
        output_a = F.dendritic_absolute_max_gate(self.y, self.dendrite_activations)
        output_b = module(self.y, self.dendrite_activations)
        all_equal = (output_a[0] == output_b[0]).all()
        self.assertTrue(all_equal)

    def test_dendritic_gate_2d(self):
        """
        Ensure `dendritic_gate_2d` and `DendriticGate2d` yield the same outputs.
        """
        module = DendriticGate2d()
        output_a = F.dendritic_gate_2d(self.y_2d, self.dendrite_activations_2d)
        output_b = module(self.y_2d, self.dendrite_activations_2d)
        all_equal = (output_a[0] == output_b[0]).all()
        self.assertTrue(all_equal)

    def test_dendritic_absolute_max_gate_2d(self):
        """
        Ensure `dendritic_absolute_max_gate_2d` and `DendriticAbsoluteMaxGate2d` yield
        the same outputs.
        """
        module = DendriticAbsoluteMaxGate2d()
        output_a = F.dendritic_absolute_max_gate_2d(self.y_2d,
                                                    self.dendrite_activations_2d)
        output_b = module(self.y_2d, self.dendrite_activations_2d)
        all_equal = (output_a[0] == output_b[0]).all()
        self.assertTrue(all_equal)


if __name__ == "__main__":
    unittest.main(verbosity=2)
