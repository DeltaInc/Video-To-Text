from dvtt.core import DVP
import sys

print("""########## Delta - Video To Text ##########""")
print("""########## Company : Dela Inc. ##########""")
print("""########## Developer : Phoenix ##########""")

if sys.argv[1] == "Audio":
    DVP(sys.argv[2]).ToAudio()

elif sys.argv[1] == "Text":
    DVP(sys.argv[2]).ToText(sys.argv[3],sys.argv[4])