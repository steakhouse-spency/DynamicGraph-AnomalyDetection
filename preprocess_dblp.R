install.packages("plyr")

## injest raw data

# node collaborations and dates
dblp = read.table("/home/thotiana/Desktop/dblp_coauthor/out.dblp_coauthor", sep = " ")

# node authors representation
node.names = read.table("/home/thotiana/Desktop/dblp_coauthor/ent.author", sep=" ", skip = 3)

# extract author name vector, use index to reprsent node number
node.names = as.character(node.names[,2])


#cleanse
dblp$V3 = NULL
dblp$V4 = NULL
names(dblp) = c("a","b","epoch")
dblp$date = as.Date(as.POSIXct(dblp$epoch, origin="1970-01-01"))
dblp$year = as.numeric(format(dblp$date, "%Y"))
dblp$date = NULL
dblp$epoch = NULL



# 2014 - 1938
unique_years = sort(unique(dblp$year), decreasing = TRUE)

# visualize density of collaboration by year
plot(density(dblp$year))
freq_years = sort(table(dblp$year), decreasing = TRUE)


# isolate collaborations that occured from 2010 - 2014
dense.dblp = dblp[dblp$year %in% 2010:2014,]
# delete all duplicates (change graph from directed to undirected)
dense.dblp = dense.dblp[dense.dblp$a < dense.dblp$b,]
# sort by year, node a, node b
dense.dblp = dense.dblp[order(dense.dblp$year, dense.dblp$a, dense.dblp$b),]


# finds the top n collaborators with most frequency in dat
# returns all collaborations between these n collaborators
top.n = function(dat, authors, n){
  # must install plyr package
  stopifnot(require(plyr))
  
  # check frequency of collaborators
  freq_node = sort(table(c(dat$a,dat$b)), decreasing = TRUE)
  
  # nodes with top n collaborators
  top = as.numeric(head(names(freq_node),n))
  
  # all collaborations/edges between top n collabortors
  top = dat[dat$a %in% top & dat$b %in% top,]
  
  # get all unique years
  years = sort(unique(top$year))
  # generate time sequences
  timeseq = 0:(length(years)-1)
  # map time sequence to year
  timeseq.years = data.frame(timeseq = timeseq, years = years)
  # stream to file
  write.table(timeseq.years, "./time.txt", sep=" ", row.names = FALSE, col.names = FALSE)
  # scale year values
  top$year = mapvalues(top$year, from=years, to=timeseq)
  
  # get all unique nodes
  nodes = sort(unique(c(top$a,top$b)))
  # map new node numbers to author names
  nodes.authors = data.frame(node = 0:(length(nodes)-1), author = authors[nodes])
  # stream to file
  write.table(nodes.authors, "./authorsTop100.txt", sep=" ", row.names = FALSE, col.names = FALSE)
  # scale node a and b values from 0 - (n-1)
  mapped = mapvalues(c(top$a,top$b), from = nodes, to = 0:(length(nodes)-1))
  len = length(mapped)
  half = len/2
  top$a = mapped[1:half]
  top$b = mapped[(half+1):len]
  
  # find frequency of node a, node b, and year combination
  edges = table(paste(top$a, top$b, top$year))
  # retrieve edge weight(frequency)
  edge.weight = as.vector(edges)
  # retrieve edge info (nodes, time)
  edge.info = names(edges)
  
  # convert to data frame
  top = as.data.frame(matrix(as.numeric(unlist(strsplit(edge.info, " "))), ncol=3, byrow=TRUE ))
  top = cbind(top, data.frame(edge.weight))
  top = top[,c(1,2,4,3)]
  names(top) = c("a", "b", "weight", "time")
  
  
  # TO DO:
  # add header totalNodes totalTimeSeq
  top = top[order(top$time, top$a, top$b),]
  write.table(top,"./graphDataTop100.txt",sep=" ", row.names = FALSE, col.names = FALSE)
  return(top)
}



check = top.n(dense.dblp, node.names, 300)
check = check[order(check$time,check$a, check$b),]
