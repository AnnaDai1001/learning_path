# Helpful webpage for setting up environment variables in Windows and Linux
# https://www.cnblogs.com/cloudtj/articles/6372197.html
# R_HOME should be "C:\Program Files\R\R-3.2.0" rather than "C:\Program Files\R\R-3.2.0\bin"

# Instead of widget: 
# import os
# os.environ["R_HOME"] = r"C:\Users\...\Documents\R\R-4.0.2" # this can be found from Tools of Rstudio > General
# os.environ["PATH"]   = r"C:\Users\...\Documents\R\R-4.0.2\bin\x64" + ";" + os.environ["PATH"]

##### r实例 #####
import rpy2
from rpy2 import robjects
from rpy2.robjects.packages import importr
import pandas as pd

r = robjects.r

##### r实例 #####
print(r['pi'])
print(r('pi'))
print(r.pi)

from rpy2.robjects import pandas2ri, packages
pandas2ri.activate()
stats = packages.importr('stats')

r(
    '''
    f <- function(r){pi * r}
    '''
)
r['f'](3)
r['ls']()
# r['fctn_name'](args)
l = r['letters']
len(l)
r['paste'](l, collapse = '-')
coder = 'paste(%s, collapse = "-")' % (l.r_repr())
r(coder)

##### 特殊的R对象比如list和matrix，如果python要调去其中的部分数据，可以通过其rx()和rx2()方法操作。
##### 对于list，可以查看其name属性，以获得列表个个元素名称。rx()和相当于"["操作（注意取出的是R的list对象），而rx2()相当于"[["操作。一个例子：
tmp = r("list(a = matrix(1:10, nrow = 2), b = 'Hello')")
print(tmp)
tmp.names
tmp.rx('a')
tmp.rx2('a')

##### Call R functions
dt_pkg = packages.importr('data.table')
# dt_pkg.fread()
plot_data = r['fread']('04_20_2021_Data.csv', 
                       encoding = 'UTF-8',
                       stringsAsFactors = False)
print(r.head(plot_data))

utils = packages.importr('utils')
utils.chooseCRANmirror(ind=1)
from rpy2.robjects.vectors import StrVector
# Install packages
packnames = ("data.table", 
             "rstudioapi",
             "lda",
             'stringr',
             'tidyverse',
             'tidytext',
             'DT',
             'tm',
             'stopwords',
             'SnowballC',
             'dplyr',
             'textclean',
             'AUC',
             'h2o')
utils.install_packages(StrVector(packnames))

r(
    '''
    text_process <- function(df_txt){
        ## fill in missing text
        df_txt[is.na(df_txt)] <- 'unknown'
        df_txt$accident_txt[df_txt$accident_txt==''] <- 'unknown' 
        df_txt$injury_txt[df_txt$injury_txt==''] <- 'unknown'

        ## remove unusable text
        df_txt$accident_txt <- stringr::str_replace_all(df_txt$accident_txt,"[^[:graph:]]", " ") 
        df_txt$injury_txt <- stringr::str_replace_all(df_txt$injury_txt,"[^[:graph:]]", " ") 

        ## word mapping
        mapping <- readRDS(file = "mapping.RDS")

        ## stopwords
        stop_add <- readRDS(file = "stop_add.RDS")
        stop_total <- unique(
          c(stop_add,
            as.vector(unlist(data_stopwords_snowball,recursive = TRUE)),
            as.vector(unlist(data_stopwords_smart,recursive = TRUE))
            )
          )
        
        ## clean text
        start_time <- Sys.time()
        df_txt_clean <- apply(df_txt[,2:3], MARGIN = c(1,2), FUN = Clean_String, stopwords_v = stop_total, level_key = mapping)
        print(Sys.time() - start_time)
        
        colnames(df_txt_clean) <- c('accident_txt_clean','injury_txt_clean')
        df_txt <- cbind(df_txt,df_txt_clean)
    }
    '''
)

df_text2 = r['text_process'](df_text)



plot_data = r['read.csv']('C:/Users/abdata/Desktop/result_test_win.csv')
print(r.head(plot_data))
mtx = r['data.matrix'](plot_data)
r.setwd("C:/Users/abdata/Desktop/")
# r.jpeg(file="myplot.jpeg")
r.png(file="myplot.png", bg="transparent")
# r.pdf(file="myplot.pdf")
r.dotchart(mtx)
r['dev.off']()

