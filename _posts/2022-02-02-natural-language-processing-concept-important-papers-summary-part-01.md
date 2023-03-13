---
layout: single
title: "Necessary Concept Papers of Natural Language Processing (NLP)"
header:
  image: "https://live.staticflickr.com/65535/52014583379_0e837e6525_o.png"
  teaser: "https://live.staticflickr.com/65535/52014583379_0e837e6525_o.png"
categories:
  - NLP
tags:
  - NLP
  - Natural language Processing
  - Concept
  - Manuscript
  - Word-2-vec
  - Glove
  - Word Representation
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post presents the summary of a few concept papers of Natural Language Processing"
---

In this post, I have added summary of a few basic concept papers of Natural Language processing. I have also included the pdf links of each paper. 

You can read the whole paper if you are interested. Otherwise you can just read the summaries in this post and undestand which papers worth reading.


### [A neural probabilistic language model](https://proceedings.neurips.cc/paper/2000/file/728f206c2a01bf572b5940d7d9a8fa4c-Paper.pdf)
-   **1st Author:** Yoshua Bengio
-   **Published:** 2003
-   **Concept:** The paper addressed the issue of curse of dimensionality by learning a distributed representation for words which allows each training sentence to train the model about several other semantically neighboring sentences. The curse of dimension is defined by the test dataset where the word sequences are entirely different or different to some degree from the training set. The contribution of the paper is two-fold: first, the model learns a distributed representation for each word sequence, and second, probability function for word sequences (representations). The goal is to achieve generalization by assigning high probability value to the sentences that is made of words that are similar. This fights against the curse of dimension as well as in terms of resource optimization, the memory requirements scale linearly, not exponentially with the number of conditioning variables.

### [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)
-   **1st Author:** Tomas Mikolov
-   **Published:** 2013
-   **Concept:** It is a very interesting paper from Google, which proposed two novel model architectures for computing continuous vector representations of words from very large data sets. The goal was to train high
quality word vectors using very simple model architectures. The authors utilized the DistBelief distributed framework to train the CBOW and Skip-gram models even on corpora with one trillion words, which takes a lot longer using the traditional neural network models (of that time). The authors achieved large improvements in accuracy at much lower computational cost, for example, learning high quality word vectors from a 1.6 billion words data set took only less than a day. The paper described two log-linear models (Continuous Bag-of-Words Model and Continuous Skip-gram model), which trains the words parallely to achieve better word representations at much higher speed.

### [Glove: Global vectors for word representation](https://aclanthology.org/D14-1162.pdf)
-   **1st Author:** Jeffrey Pennington
-   **Published:** 2014
-   **Concept:** In this paper, the authors presented a new global log-bilinear regression model that combines the advantages of the two major model families in the literature: global matrix factorization and local context window methods. Authors claimed that their model efficiently leverages statistical information by training only on the nonzero elements in a word-word co-occurrence matrix, rather than considering the entire sparse matrix or considering individual context windows in a large corpus. There are two types of word representations: count-based and prediction-based. Authors claimed that the prediction-based methods work better for word representations. However, they utilized the main benefit of count data while simultaneously capturing the meaningful linear substructures utilized within some log-bilinear prediction-based methods (e.g., word2vec).

### [Distributed representations of sentences and documents](http://proceedings.mlr.press/v32/le14.pdf)
-   **1st Author:** Quoc Le
-   **Published:** 2014
-   **Concept:** The paper presented Paragraph Vector, an unsupervised algorithm that learns fixed-length feature representations from variable-length pieces of texts. Here, variable-length pieces of texts can be sentences, paragraphs, and documents. Authors claimed that the `bag-of-words` features have two major weaknesses: they lose the ordering of the words and they also ignore semantics of the words which is crucial for context. Therefore, the task is to represent each document by a dense vector which is trained to predict words in the document. The authors showed that Paragraph Vectors outperforms bag-of-words models for text representations. 
Here, Paragraph Vector learns vector representations for variable length pieces of texts such as sentences and documents. The primary goal of the vector representations is to predict the neighboring words in contexts sampled from the paragraph. Paragraph vector method has the potential for variable length text classification and generation in applied NLP tasks.

### [Enriching Word Vectors with Subword Information](https://watermark.silverchair.com/tacl_a_00051.pdf)
-   **1st Author:** Piotr Bojanowski
-   **Published:** 2017
-   **Concept:** In this paper, the authors proposed a new approach based on the skipgram model, where each word is represented as a bag of character n-grams. Continuous word representations is quite useful for different types of NLP tasks. Usually, these representations are trained on the basis of large unlabeled corpora. Here, each word is represented as a vector (such as word-2-vec). However, in this work, A vector representation is associated to each character n-gram. That means the words are represented as the sum of these representations. The authors claimed that the proposed method works faster that existing methods for large volume of datasets. The approach basically incorporates character n-grams into the skipgram model and process the subword information by training on basis of subword representations.

### [Learning representations by back-propagating errors](https://www.nature.com/articles/323533a0.pdf)
-   **1st Author:** David E. Rumelhart
-   **Published:** 1986
-   **Concept:** This paper is an early-generation paper on the context of neural network. Here, the authors described a new learning procedure and back-propagation, for networks of neurons. The procedure repeatedly adjusts the weights of the connections in the network to minimize error and difference between the actual and desired output vectors.
The method calculates the gradient of the error function with respect to the neural network's weights when given an artificial neural network and an error function. The primary implication is to train a feed-forward network. Backpropagation uses the gradient of the loss function with respect to the weights of the neuron. So basically, the main purpose of back-propagation is to compute the gradient. The authors explained the representation of the errors.

### [Word2Vec Parameter learning explained](https://arxiv.org/pdf/1411.2738.pdf)
-   **1st Author:** Xin Rong
-   **Published:** 2014
-   **Concept:** The author writes a tutorial for the researchers to understand the basics of  word2vec model and applications. The author noticed a lack of useful resources and thus presented the the parameter learning process of word embedding models in details. The author provided a detailed derivations and explanations of the parameter update equations of the word2vec models, including the original continuous bag-of-word (CBOW) and skip-gram (SG) models. The author also included advanced optimization techniques, including hierarchical softmax and negative sampling. This paper is very helpful for beginner researchers like us to get into the word embedding and representations research. First, the author discussed the CBOW, where he discussed one-word and multi-word context. Then the author discussed the skip-gram model. And finally, the optimization of Computational Efficiency through hierarchical softmax and negative sampling.

### [Distributed Representations of Words and Phrases and their Compositionality](https://proceedings.neurips.cc/paper/2013/file/9aa42b31882ec039965f3c4923ce901b-Paper.pdf)
-   **1st Author:** Tomas Mikolov
-   **Published:** 2013
-   **Concept:** This paper is an improvement and extension over the previously published continuous Skip-gram model (described earlier-the Google paper). Here, they improved the quality of the vectors as well as the training speed. The speedup works by subsampling of the frequent words. Another extension is using negative sampling instead of hierarchical softmax.

### [Data quality dimensions for information systems security: A theoretical exposition](https://link.springer.com/content/pdf/10.1007/0-387-31167-X_2.pdf)
-   **1st Author:** Gurvirender Tejay
-   **Published:** 2004
-   **Concept:** The paper suggests that data, information, or knowledge quality is vital for ensuring the safety of different information systems. Authors argued that the nature and scope of data quality dimensions changes as we move between different semiotic levels. Authors first discussed the relationship between signs, data and IS security. Authors utilized Semiotics as a frame of reference to define the concepts of data and information to allow analyzing the dimensions of data quality. Authors suggested using semiotics as a theoretical basis for addressing the inherent complexity of data. There are a few semiotic levels: pragmatics, semantics, syntactics, and empirics. Empirics analyzes  the physical properties of signs (signals used to code and transmit the message). Syntactics comprises of logic and grammar of sign systems. Semantics is all about the meaning of these signs. And pragmatics deals with the relationships between signs and behavior in a given context. Authors then provided a list of dimensions for each of these concepts and map with different seminal work. The key takeaway from the paper is: Semiotics assists us to unravel and understand the inter-dependent nature of data, information and knowledge as well as provides a clear understanding of the dimensions associated with the data quality.



### [Hierarchical Attention Networks for Document Classification](https://aclanthology.org/N16-1174.pdf)
-   **1st Author:** Zichao Yang
-   **Published:** 2016
-   **Concept:** In this paper, the authors utilized a hierarchical attention network (HAN) for document classification. Here, they reconstruct the document representation based on the hierarchical structure (e.g., words to sentence, sentence to documents). To do that, they first construct the representation of the sentences, and then aggregates these representations to reconstruct the document representations. As sentences tend to be differentially informative, the authors focused more on context sensitivity and therefore, included two levels of attention mechanisms (Bahdanau et al., 2014; Xu et al., 2015): word level and sentence level. So, basically the idea is to aggregate only the most important contents by building a document vector by aggregating important words into sentence vectors and then aggregating important sentences vectors to document vectors.

### [Convolutional Neural Networks for Sentence Classification](https://uwspace.uwaterloo.ca/bitstream/handle/10012/9592/Chen_Yahui.pdf)
-   **1st Author:** Yoon Kim
-   **Published:** 2014
-   **Concept:** This paper shows that convolutional neural networks (CNN) can be used for sentence-level classification when trained on top of pre-trained word vectors. CNN is usually popular for image classification tasks. However, the authors showed that, it worked better than the state-of-the-art models including RAE, MV-RNN, RNTN, SVM, etc. when applied on some dataset. The author showed that CNN-multichannel worked best for two dataset, and CNN-static and CNN-nonstatic worked best for one dataset among the tested seven. The primary learning point was it is possible to utilize CNN with some tuned hyper-parameters for sentence-level classification which is important for security-oriented tasks (e.g., anonymization, privacy-aware data scrambling, etc.), recommendation engines, and sentiment analysis.

In the next part, I will add summary of a few state-of-the-art papers.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ3MzAxMDUyLC0xNDc3NTY4NDU5XX0=
-->