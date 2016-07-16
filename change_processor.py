# The variable sep looks for lines that have 72 - hyphens.

sep = 72*'-'

# the class to process changes
# initialise itself using self which will be used to read in the file.
class ChangeProcessor(object):

    def __init__(self, file_name):
        self.read_file(file_name)


    # use strip to strip out spaces and trim the line.
    # the return gets the length of the file being tested.
    def read_file(self, file_name):
        self.data = [line.strip() for line in open(file_name, 'r')]
        self.process_commits()
        return len(self.data)

    # function used for processing the commits.  1st sets up a list called commits and a dictionary called authors.
    # current_commit is given the initialisation value of None because it hasn't run yet and it needs to hold a default
    # variable.  The variable index is initialised at 0 this will be used to iterate to the next commit. 
    # The while True loop will be used for going between commits and taking the needed data e.g. author, index.
    # The try/except is a safety measure incase there is a problem with the file the IndexError will be used and
    # break out of the while loop.    
    def process_commits(self):
        self.commits = []
        self.authors = {}
        current_commit = None
        index = 0

        while True:
            try:
                # parse each of the commits and put them into a list of commits.  The details is split on the bar
                # | character.
                details = self.data[index + 1].split('|')
                details = [column.strip() for column in details]

                # the file changes with spaces at end removed.
                details.append(self.data[index+2:self.data.index('',index+1)])

                # add details to the list of commits.
                self.commits.append(details)
                index = self.data.index(sep, index + 1)
                # If the authors not in the dictionary the author is added to the dictionary with a value of 1.  If
                # the author is already in the dictionary the value for the key (author) is incremented by 1.
                if details[1] not in self.authors:
                    self.authors[details[1]] = 1
                else:
                    self.authors[details[1]] = self.authors[details[1]] + 1

                comment_line_count = int(details[3].strip().split(' ')[0])
                # add the comments to the details.
                details.append(self.data[index-comment_line_count:index])

            except IndexError:
                break

    # The get author function gets the author which is in index position 1 of commits or the 2 element.  For get_date the position is 2,
    # number_of_comment_lines is 3, revision is index position 0, file_changes is index positon 4 or 5th element.   
    def get_author(self, index):
        return self.commits[index][1]

    def get_date(self, index):
        return self.commits[index][2]

    def get_number_of_comment_lines(self, index):
        return self.commits[index][3]

    def get_revision(self, index):
        return self.commits[index][0]

    def get_file_changes(self, index):
        return self.commits[index][4]

    def get_comment(self, index):
        return self.commits[index][5]

        
    # function for returning the number of commits in the file using the len function.
    # 2nd function counts the number of authors in the file.
    # 3rd function gets what the specific author commited to the file.
    def get_number_of_commits(self):
        return len(self.commits)

    def get_number_of_authors(self):
        return len(self.authors)

    def get_number_of_commit_by_author(self, author):
        return self.authors[author]