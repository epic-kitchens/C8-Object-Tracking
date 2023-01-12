import sys
sys.path.append('./TREK-150-toolkit')

from tracker import YourTracker
from toolkit.experiments import ExperimentTREK150

tracker = YourTracker()

root_dir = './' # set the path to TREK-150's root folder
exp = ExperimentTREK150(root_dir, result_dir='./', report_dir='./')

exp.export_results_for_challenge(tracker.name)