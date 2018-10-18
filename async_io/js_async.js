

//co自动执行器的原理


//手动执行
var gen = function* () {
  var f1 = yield readFile('/etc/fstab');
  var f2 = yield readFile('/etc/shells');
  console.log(f1.toString());
  console.log(f2.toString());
};

var g = gen();
g.next().value.then(function(data){
  g.next(data).value.then(function(data){
    g.next(data);
  });
});


//自动执行
function run(gen){
  var g = gen();

  function next(data){
    var result = g.next(data);
    if (result.done) return result.value;
    result.value.then(function(data){
      next(data);
    });
  }

  next();
}

run(gen);





