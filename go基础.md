## 一些设计思想 ##
什么东西都去GOPATH下面找比较好  
什么东西都去github下面找比较方便  

## 信息 ##
阅读文档  
https://godoc.org/

## 安装 ##
https://golang.org/dl/  
setpath

## 基础 ##
1. 所有go语言编译的可执行程序都必须有一个名叫main的包，并且里面有main()
2. 查看包的帮助文档
godoc fmt | less
3. 包都在GOPATH/src下面去找
4. 如果是import "github.com/spf13/viper"之类的import的话，会用toolchains里面的go get从网络上获取，保存到本地的$GOPATH里面，下次就可以直接用了。
5. 同名包的处理
`import (
    "fmt"
    "mylib/fmt"
)
`
6. go不允许引入不用的包，直接报错，这**跟C报warning不一样**，更加干净，毕竟C的warning太多了。
引入而不使用标识符就用_
7. 每个包可以包含任意多个 init 函数，这些函数都会在程序执行开始的时候被调用。所有被编译器发现的 init 函数都会安排在 main 函数之前执行。init 函数用在设置包、初始化变量或者其他要在程序运行前优先完成的引导工作。
8. go vet能找出一下常见错误
9. godoc -http=:6060 查看go文档，与github上同步更新
10. 有很多社区开发的依赖管理工具，如 godep、vender 和 gb
11. 数组是一种非常有用的数据结构，因为其占用的内存是连续分配的。由于内存连续，CPU能把正在使用的数据缓存更久的时间。而且内存连续很容易计算索引，可以快速迭代数组里的所有元素。数组的类型信息可以提供每次访问一个元素时需要在内存中移动的距离。既然数组的每个元素类型相同，又是连续分配，就可以以固定速度索引数组中的任意数据，速度非常快。**局部性原理应用的最好**。
12. **所有变量都会默认初始化，而C不是**
13. 数组本身只有一个维度，不过可以组合多个数组创建多维数组。多维数组很容易管理具有父子关系的数据或者与坐标系相关联的数据。
14. 切片与数组的区别，切片不需要指定大小。数组 var [3]int;   切片 var []int
15. **切片的容量的作用，append的时候不用每次realloc，提高效率，类似于hash表的容量的实现**
16. 用range遍历切片时，range 是创建了每个元素的副本，而不是直接返回对该元素的引用
17. 结构的方法：方法能给用户定义的类型添加新的行为。方法实际上也是函数，只是在声明时，在关键字func 和方法名之间增加了一个参数。关键字 func 和函数名之间的参数被称作接收者，将函数与接收者的类型绑在一起。如果一个函数有接收者，这个函数就被称为方法。
18. 内置类型是由语言提供的一组类型。我们已经见过这些类型，分别是数值类型、字符串类型和布尔类型。
19. Go 语言里的引用类型有如下几个：切片、映射、通道、接口和函数类型。
20. 嵌入类型，内部结构都获得提升，但是外部可以覆盖。嵌入类型提供了扩展类型的能力，而无需使用继承。
21. defer可以写在函数任意地方，运行的时候能保证这个函数返回的时候肯定能调用。  
22. main函数也是一个goroutine，协程。一个channel要么被另一个协程读取要么被main函数读取。  
23. 编译调试版本： go build -gcflags "-N -l"。  
24. 单元测试：名字要以_test.go结尾，执行 go test，若想看详细信息则go test -v. t.Fatal会结束当前测试用例，即当前测试函数，因为 t.Errorf 方法不会停止当前测试函数的执行，所以单元测试就会继续执行。如果测试函数执行时没有调用过 t.Fatal或者 t.Error 方法，就会认为测试通过了。**原理非常简洁。**  
25. 标准库的学习。。。。。。  
