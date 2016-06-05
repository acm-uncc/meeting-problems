input = [[5,6,7], [3,9,4], [1,8,4,6,8,2], [2]]

product = 1

input.each do | inner |
  inner.each do | num |
    product *= num
  end
end

puts product
