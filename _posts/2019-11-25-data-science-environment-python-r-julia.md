---
layout: single
title: "Data Science Work Environment setup on Linux/Mac"
header:
  image: "https://live.staticflickr.com/65535/49155021077_42b4a1bc81_h.jpg"
  teaser: "https://live.staticflickr.com/65535/49155021077_42b4a1bc81_h.jpg"
categories:
  - Data Science
tags:
  - Conda
  - Python
  - R Language
  - Julia
  - Data Science
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


`Python`, `R`, and `Julia`- these languages are usually used in data science projects. In this tutorial we will see how to create a proper environment for working on data science projects.

## Conda environment setup
We can directly install any language on the system. However, it is recommended to use virtual environments to avoid conflicts between using different versions of same language. For that purpose, we will use [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). We can use [Anaconda](https://www.anaconda.com/distribution/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html). I prefer `Miniconda` because it is lightweight and does not come with all the packages making the machine heavy. That means we will have to install packages if we need them. In `Anaconda`, all packages are installed by default.

### Install Miniconda
* Download and install miniconda form [here](https://docs.conda.io/en/latest/miniconda.html)

* Last step enter `no` when prompted with the following message:
  ```
  Do you wish the installer to prepend the conda install location to PATH in your /root/.bashrc ? [yes|no]
  ```

* Symbolic link creation for `conda` command
	* Create a hidden directory in user's home directory
	```bash
    $ cd ~
    $ mkdir .conda_links
    $ cd .conda_links
    ```
    * Create symbolic links (Linux)
    ```bash
    $ ln -s /home/$USER/miniconda3/bin/conda conda
	$ ln -s /home/$USER/miniconda3/bin/activate activate
	$ ln -s /home/$USER/miniconda3/bin/deactivate deactivate
    ```
    * Create symbolic links (Mac)
    Use your username instead of `roy`.
    ```bash
    $ ln -s /Users/roy/miniconda3/bin/conda conda
	$ ln -s /Users/roy/miniconda3/bin/activate activate
	$ ln -s /Users/roy/miniconda3/bin/deactivate deactivate
    ```
    * In `~/.bashrc` file, add the following (Linux)
    ```sh
    export PATH=/home/roy/.conda_links:$PATH
    ```
    * In `~/.bash_profile` file, add the following (Mac)
    ```sh
    export PATH=/Users/roy/.conda_links:$PATH
    ```

* Check installation of `conda`
```bash
$ conda --version
```

### Environment Setup
* Create a `python` virtual environment (my_lab is environment name and python version is 3.6)
```bash
$ conda create --name my_lab python=3.6
```
* Check environment with following command:
```bash
$ conda info --envs
```
* Activate environment
```bash
$ source activate my_lab
```
* Deactivate environment
```bash
$ source deactivate
```
* Delete existing environment
```bash
$ conda remove --name my_lab --all
```

## IDE setup
### Install Jupyter Notebook
```bash
$ pip install --upgrade pip
$ pip install --upgrade ipython jupyter
$ jupyter notebook
```

### Install Jupyter Lab
`Jupyter Lab` has a better IDE alike features than `Jupyter Notebook`. Jupyter notebook is good enough for beginners. Advanced users may prefer Jupyter Lab over notebook.
```bash
$ pip install jupyterlab
```

## Language Setup
`Conda` comes with `python` kernel by default. `R` and `Julia` kernels can be installed alongside. List of jupyter kernels is available in the official [git repo](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).

### Install Julia Kernel
* Download [**Julia**](https://julialang.org/downloads/) and install
* Run Julia CLI
* Enter the following commands:
```bash
julia> using Pkg
julia> Pkg.add("IJulia")
```
Now, julia will be available in Jupyter notebook/lab.

### Install R kernel
* Download [**R**](https://cran.r-project.org/mirrors.html) and install
* Run R CLI
* Enter the following commands:
```bash
R> install.packages('IRkernel')
R> IRkernel::installspec()
```
Optional:
```bash
R> IRkernel::installspec(name = 'ir33', displayname = 'R 3.3')
```

## Professional IDE
| Language | IDE |
| :------------- | :----------: |
| Python | [**PyCharm**](https://www.jetbrains.com/pycharm/download) |
| R | [**R Studio**](https://rstudio.com/products/rstudio/download/) |
| Julia | [**Julia Studio**](https://www.linuxlinks.com/juliastudio/) |

## References
* [Installing chatterbot in conda environment using Python 3.7](https://gist.github.com/arsho/9a1e4ac9221c50d754a90a7291a12602)
* [Install JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
* [How to Add Julia to Jupyter Notebook](https://datatofish.com/add-julia-to-jupyter/)
* [Native R kernel for Jupyter](https://github.com/IRkernel/IRkernel)