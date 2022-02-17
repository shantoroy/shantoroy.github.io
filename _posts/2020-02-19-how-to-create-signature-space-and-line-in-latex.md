---
layout: single
title: "How to add a Signature line and Space in Latex"
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/51887360931_5dfb39dbd7_o.png"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Table
  - How-to
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post explains how to add a Signature line and Space in any Latex Document"
---


If you need to add a signature space and line, just create a table of one column. You can do it without creating a table too, however, it helps if you need additional customization in the left or right side.

In the following code, `\vspace{25mm}` is used to have a space for the signature. You can customize the number according to your need.

Later, `\hrulefill` is used to fill up the size of the column with a horizontal line. Here, I used $2.5$ inches. Customize it based on your need.

```latex
\vspace{25mm}
\begin{tabular}{@{}p{2.5in}@{}}
\hrulefill \\
Shanto Roy \\
University of Houston
\end{tabular}
```

If you want to add a date in thr right side, just add two extra columns in the table: the first one to have extra space in the middle, and the last column includes the date.
```latex
\vspace{25mm}
\begin{tabular}{@{}p{2.5in}p{2in}p{2in}@{}}
\hrulefill && Date: 17 February, 2022\\
Shanto Roy &&\\
University of Houston
\end{tabular}
```

That's all, cheers!
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzU3Mjc4ODA3XX0=
-->