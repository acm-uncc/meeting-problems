const input = [[5,6,7], [3,9,4], [1,8,4,6,8,2], [2]];

var product = 1;

input.forEach((inner) => {
  inner.forEach((num) => {
    product *= num;
  });
});

console.log(product);
