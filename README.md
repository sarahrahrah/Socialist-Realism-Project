# Socialist Realism Text Analysis Project


This digital humanities project uses text analysis techniques to examine the characteristics of Soviet socialist realism of the pre-WII era.  

Logistic regression and topic modeling were used to examine the corpora.  The scripts prediction.py and topicmodeling.py contain these techniques, applied to the corpora.  The jupyter notebook (socialist-realism-project-notebook.ipynb) also contains the analysis, with some visualization.

The folders chunking_scripts, aggregation_scripts, and NER_script all contain various python scripts that were used to prepare the .csv files used in the analysis.  The chunking scripts divide the individual text files into subsections, and the aggregation scripts put the chunked files into .csv format.  The NER_script uses the spaCy library for Named Entity Recognition (NER) and extraction into the NER text files that are used in the analysis. 

The following python libraries were used in the analysis:

- nltk
- gensim
- plotly
- sklearn
- matplotlib 
- pymystem
- pyLDAvis
