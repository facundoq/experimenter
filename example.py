from experimenter import Experiment

results_folderpath="results"

class MyExperiment(Experiment):

    def __init__(self):
        super().__init__(results_folderpath)
    
     

class Example1(MyExperiment):

    def run(self):
        result = "My Result"
        print(result)
        
    description = "A simple experiment that prints"        
    tags =  ["simple","print"]
            
        
class Example2(MyExperiment):

    def run(self):
        result = "My Result"
        with open(self.folderpath/"result.txt","w") as f:
            f.write(result)
    description = "A simple experiment that uses a file"
    tags =  ["simple","files"]
        


if __name__ == '__main__':
    experiments = [Example1(),Example2()]
    Experiment.main(experiments)
    
    