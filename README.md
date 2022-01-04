# EDURELL - Knowledge extraction from video
<p>The goal is to identify concepts, compute their relevance and track them along the video flow. By given an educational video, the program detects (if there are any) the person who appeared the most (in our case the speaker), the scene that we are most likely looking at (blackboard, slide, slide-and-talk, talk) and extracts texts. 

## Setup
<br />
<b>Step 1.</b> Clone this repository: https://github.com/Gabbosaur/SWT-AggregateLD
<br/><br/>
<b>Step 2.</b> Create a new virtual environment 
<pre>
python -m venv edurell
</pre> 
<br/>
<b>Step 3.</b> Activate your virtual environment
<pre>
source tfod/bin/activate # Linux
.\tfod\Scripts\activate # Windows 
</pre>
<br/>
<b>Step 4.</b> Install libraries used in the project
<br/>
<b>Step 5.</b> Set video filename to be processed
<br/>
