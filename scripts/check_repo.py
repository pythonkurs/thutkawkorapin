import os
import sys
from thutkawkorapin.session3 import CourseRepo, set_repo_dir

test_dir = sys.argv[1]
final_part = os.path.basename(os.path.split(os.path.join(sys.argv[1], ''))[0])

with set_repo_dir(test_dir):
    course_repo = CourseRepo(final_part)
    if course_repo.check():
        print 'PASS'
    else:
        print 'FAIL'

