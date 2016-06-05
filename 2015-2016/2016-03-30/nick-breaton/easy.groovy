def input = [[5,6,7], [3,9,4], [1,8,4,6,8,2], [2]]

int product = 1

input.each {
  it.each {
    product *= it
  }
}

println product
