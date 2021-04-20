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
plot_data = r['read.csv']('C:/Users/abdata/Desktop/result_test_win.csv')
print(r.head(plot_data))
mtx = r['data.matrix'](plot_data)
r.setwd("C:/Users/abdata/Desktop/")
# r.jpeg(file="myplot.jpeg")
r.png(file="myplot.png", bg="transparent")
# r.pdf(file="myplot.pdf")
r.dotchart(mtx)
r['dev.off']()
