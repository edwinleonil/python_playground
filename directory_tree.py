from bigtree import list_to_tree
import sys

path_list = ["amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-TransferLearning/Data/Images/Image1.png",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-TransferLearning/Data/Images/Image2.png",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-TransferLearning/Data/Images/Image3.png",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-TransferLearning/Data/Images/Image ... ",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-TransferLearning/Helpers/helper1.py",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-TransferLearning/Helpers/helper2.py",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-TransferLearning/Helpers/helper3.py",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-TransferLearning/Helpers/helper ... ",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-TransferLearning/Main/main1.py",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-TransferLearning/requirements.txt",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-TransferLearning/README.md",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-AutoReportGeneration/Data/Images/Image1.png",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-AutoReportGeneration/Data/Images/Image2.png",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-AutoReportGeneration/Data/Images/Image3.png",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-AutoReportGeneration/Data/Images/Image ... ",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-AutoReportGeneration/Helpers/helper1.py",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-AutoReportGeneration/Helpers/helper2.py",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-AutoReportGeneration/Helpers/helper3.py",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-AutoReportGeneration/Helpers/helper ... ",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-AutoReportGeneration/Main/main1.py",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-AutoReportGeneration/requirements.txt",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-AutoReportGeneration/README.md",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-LabelingApp/Data/Images/Image1.png",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-LabelingApp/Data/Images/Image2.png",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-LabelingApp/Data/Images/Image3.png",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-LabelingApp/Data/Images/Image ... ",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-LabelingApp/Helpers/helper1.py",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-LabelingApp/Helpers/helper2.py",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-LabelingApp/Helpers/helper3.py",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-LabelingApp/Helpers/helper ... ",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-LabelingApp/Main/main1.py",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-LabelingApp/requirements.txt",
             "amrcgithub.shef.ac.uk/IMG:/AI-23-19-AVI-LabelingApp/README.md"
             ]

root = list_to_tree(path_list, sep="/",)  # create the tree

# Redirect stdout to a txt file
sys.stdout = open('GitHub_Tree.txt', 'w', encoding='utf-8')
# Print the tree
root.show()
# Close the file
sys.stdout.close()
