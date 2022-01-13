#!/usr/bin/env bash

#n=1
#while [ $n -le 5 ]; do
#  echo "Iteration number $n"
#  ((n+=1))
#done

#run while python random function doesn't return 0 or until you have completed 5 iterations
n=0
command=$1
# $1 gets the first argument in command line
while ! $command && [ $n -le 5 ]; do
  sleep $n
  ((n+=1))
  echo "Retry #$n"
done


#for loops to change every filename some way.
for file in *.HTM; do
  name=$(basename "$file" .HTM)
  mv "$file" "$name.html"
done


