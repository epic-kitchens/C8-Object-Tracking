import sys
sys.path.append('./TREK-150-toolkit')

from toolkit.trackers import Tracker

class YourTracker(Tracker):

    def __init__(self):
        super(YourTracker, self).__init__(name='YourTrackerName',)

    def init(self, image, box):
        # Implement here the initialization step of your tracker
        ...

    def update(self, image):
        # Implement here the step that executes your tracker at every frame after the initialization
        ...

        return box