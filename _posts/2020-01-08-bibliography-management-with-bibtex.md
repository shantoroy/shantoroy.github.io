---
layout: single
title: "Bibliography management with Bibtex in Latex"
excerpt:  "Bibliography management is an essential aspect of academic writing, particularly when you have to reference a large number of sources. Bibtex is a widely-used software tool for managing bibliographies and citations in Latex documents. In this blog post, I will explore how to use Bibtex to create and manage a bibliography in a Latex document." 
seo_title:  "Bibliography Management with Bibtex in Latex: A Comprehensive Guide"
seo_description:  "Learn how to manage and create a bibliography in a Latex document using Bibtex. Our comprehensive guide will help you get started with Bibtex, from importing references to formatting your bibliography in your preferred citation style."
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Bibtex
  - Documentation
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---
In this post, we will learn how to manage bibliography using BibTex in Latex. This is the most convenient way to use references in a document and also while moving from one template to another one. The only thing you will have to do is changing the bibliography style that requires one line of change.

## Add a `bibliography` File
* Create a `bibliography` file with `.bib` extension. For example: `references.bib`
* Add the file in the main `tex` file as follows:
	```latex
	\bibliographystyle{plain}
	\bibliography{references}
	```
* You can simply use the `bibliography style` as `plain`. In case you are using a particular journal/conference template, use their style file. A style file has the `.bst` extension. For example, in IEEE template you will find `ieeetran.bst` style file. Then the code will look like as follows:
	```latex
	\bibliographystyle{ieeetran}
	\bibliography{references}
	```

## Add Bibliographic Entry in `.bib` File
### For Journals/Conferences/Books
* Go to [Google Scholar](https://scholar.google.com/)
* Write the title of your article/conference proceeding/book and press Enter. For example, you want to cite the paper entitled `Information loss in black holes`. So, write the title in the search box and hit Enter. You will get the following output.
<figure>
<a href="https://live.staticflickr.com/65535/49353950636_e5647fe4b3_b.jpg"><img src="https://live.staticflickr.com/65535/49353950636_e5647fe4b3_b.jpg"></a>
</figure>


* Now click on the `double quotation mark` as follows. 
<figure>
<a href="https://live.staticflickr.com/65535/49353950651_ca5b31c62d_b.jpg"><img src="https://live.staticflickr.com/65535/49353950651_ca5b31c62d_b.jpg"></a>
</figure>

* A new dialog box will appear. Then click on the `BibTeX` link.
<figure>
<a href="https://live.staticflickr.com/65535/49354164847_aebd81f71b_b.jpg"><img src="https://live.staticflickr.com/65535/49354164847_aebd81f71b_b.jpg"></a>
</figure>

* Copy the whole entry using `Ctrl+A` and `Ctrl+C`. The entry will look like as follows:
	```latex
	@article{hawking2005information,
	  title={Information loss in black holes},
	  author={Hawking, Stephen W},
	  journal={Physical Review D},
	  volume={72},
	  number={8},
	  pages={084013},
	  year={2005},
	  publisher={APS}
	}
	```
* Paste it in your `.bib` file. Then, in the main file cite like this:
	```latex
	Hawking et al.\ proposed... ~\cite{hawking2005information}.
	```

### For Online Links
* Install an extension- [BibTeX entry from URL](https://chrome.google.com/webstore/detail/bibtex-entry-from-url/mgpmgkhhbjgkpnanlmlhibjfgpdpgjec?hl=en) in your Chrome browser or  [Bibitnow!](https://addons.mozilla.org/en-US/firefox/addon/bibitnow/) add-on in your firefox.
* Go to the page you want to cite.
* Click on the extension. The entry will be copied to clipboard.
* Paste the entry in the `.bib` file.
* Cite as before.

> That's all folks. Cheers! :sunglasses:


## Related posts on Latex
You can find a comprehensive list of Latex resources in the following post:

[Latex Resources in a Nutshell](https://shantoroy.com/latex/latex-resources-in-a-nutshell/)

If you are a new Latex user, check out this post:
[20 Most Common Mistakes Made by New Latex Users](https://shantoroy.com/latex/common-mistakes-made-by-new-latex-typesetting-users/)

You can find all `Latex` oriented posts of mine in: [https://shantoroy.com/categories/#latex](https://shantoroy.com/categories/#latex)
* [Add Copyright Notice and Conference Name in IEEE Conference Template](https://shantoroy.com/latex/add-copyright-conference-name/)
* [Preparing Tables for Publication and Documentation in Latex](https://shantoroy.com/latex/how-to-create-tables-in-latex/)
* [Creating Bar Charts using Latex PGFPlots](https://shantoroy.com/latex/bar-plots-in-latex-pgfplot/)
* [How to write an algorithm in Latex](https://shantoroy.com/latex/how-to-write-algorithm-in-latex/)
* [How to add subfigure in Latex](https://shantoroy.com/latex/how-to-add-subfig-in-latex/)
* [How to Write Matrix with Row/Column Labels in Latex](https://shantoroy.com/latex/matrix-labeling-in-latex/)
* [How to Collaboratively Write a Paper using Overleaf Latex Platform](https://shantoroy.com/latex/how-to-collaborately-write-a-paper-using-latex-overleaf/)
* [Itemize, Enumerate, and To-do-list in Latex](https://shantoroy.com/latex/playing-with-latex-itemize-enumerate-fontawesome/)
* [Latex Table for Survey in IEEE two-column format](https://shantoroy.com/latex/latex-table-for-survey-ieee-template/)
* [Line Plotting using Latex PGFPlots](https://shantoroy.com/latex/how-to-draw-line-graph-using-pgfplots-latex/)
* [How to add Codes in Latex:  `listings`  package for code documentation](https://shantoroy.com/latex/how-to-add-codes-in-latex-listing-package/)
* [Creating Multiple Line plots from CSV file using Latex Tikz and PGFPlot](https://shantoroy.com/latex/multiple-line-plots-using-tikz-pgfplot/)



<!--stackedit_data:
eyJoaXN0b3J5IjpbMjk0ODE0MDc2LC0xMjExMTQ4NDg2LC0xOT
Q5NDEzOTU0LC0xNTg1OTMzMzk5LDEzOTIzNTMwNzEsNTA3MDY3
OTAwXX0=
-->