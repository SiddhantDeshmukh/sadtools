from typing import Dict
import numpy as np


# -------------------------------------------------------------------------
# Dictionary utility functions
# -------------------------------------------------------------------------
def convert_log_dict_to_linear(log_dict: Dict):
	linear_dict = {}

	for key, value in log_dict.items():
		linear_dict[key] = 10**value

	return linear_dict


def add_unit_to_dict_items(dictionary: Dict, unit):
	unit_dict = {}

	for key, value in dictionary.items():
		unit_dict[key] = value * unit

	return unit_dict


# -------------------------------------------------------------------------
# Numerics
# -------------------------------------------------------------------------
def log10_dict(d: Dict) -> Dict:
	return {k: np.log10(v) for k, v in d.items()}

def compute_dict_mean(d: Dict, axis=(1, 2)) -> Dict:
	return {k: np.mean(v, axis=axis) for k, v in d.items()}

def compute_dict_difference(d1: Dict, d2: Dict) -> Dict:
	return {k: d1[k] - d2[k] for k in d1}