Optimisation has become a need of the hour. Monitoring GPU %,RAM usage, Temperature of GPU etc are a great indicator of how a process happens. This project allows you to run a process analysing algorithm in a parallel thread while you are running your main code/deep learning model or any code block in python that needs to be monitored. A graph will be generated once the process completes and will be saved in the same folder as your python script.

**Instructions to deploy :**

1)Import the library

say you import it as benchmarking

Then,

2)Type 

benchmarking.analyzer.start_recording()

at the point where you want to initilise the performance analysis.

3)Type

benchmarking.analyzer.stop_recording()

at the point where you want to stop the benchmarking process.

NOTE:A folder named temporary_file.txt will be created in your directory you may choose to keep it or delete it
