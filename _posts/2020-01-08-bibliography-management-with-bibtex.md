---
layout: single
title: "Bibliography management with Bibtex in Latex"
header:
  image: "https://live.staticflickr.com/65535/49353529713_7567417ff3_b.jpg"
  teaser: "https://live.staticflickr.com/65535/49353529713_7567417ff3_b.jpg"
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

If this post helps you to solve your problem, and you want to thank/support me for that, you can  [Buy me Coffee](https://www.paypal.me/shantoroy). :smiley:
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEzNDk5Mzk0NSwtMTIxMTE0ODQ4NiwtMT
k0OTQxMzk1NCwtMTU4NTkzMzM5OSwxMzkyMzUzMDcxLDUwNzA2
NzkwMF19
-->