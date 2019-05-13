# DaysBank

## 操作内容

### 反编译字节码

```js
contract Contract {
    function main() {
        memory[0x40:0x60] = 0x80;
    
        if (msg.data.length < 0x04) { revert(memory[0x00:0x00]); }
    
        var var0 = msg.data[0x00:0x20] / 0x0100000000000000000000000000000000000000000000000000000000 & 0xffffffff;
    
        if (var0 == 0x652e9d91) {
            // Dispatch table entry for 0x652e9d91 (unknown)
            var var1 = msg.value;
        
            if (var1) { revert(memory[0x00:0x00]); }
        
            var1 = 0x009c;
            func_01DC();
            stop();
        } else if (var0 == 0x66d16cc3) {
            // Dispatch table entry for profit()
            var1 = msg.value;
        
            if (var1) { revert(memory[0x00:0x00]); }
        
            var1 = 0x009c;
            profit();
            stop();
        } else if (var0 == 0x6bc344bc) {
            // Dispatch table entry for 0x6bc344bc (payforflag(string))
            var1 = msg.value;
        
            if (var1) { revert(memory[0x00:0x00]); }
        
            var temp0 = memory[0x40:0x60];
            var temp1 = msg.data[0x04:0x24];
            var temp2 = msg.data[temp1 + 0x04:temp1 + 0x04 + 0x20];
            memory[0x40:0x60] = temp0 + (temp2 + 0x1f) / 0x20 * 0x20 + 0x20;
            memory[temp0:temp0 + 0x20] = temp2;
            var1 = 0x009c;
            memory[temp0 + 0x20:temp0 + 0x20 + temp2] = msg.data[temp1 + 0x24:temp1 + 0x24 + temp2];
            var var2 = temp0;
            func_0278(var2);
            stop();
        } else if (var0 == 0x70a08231) {
            // Dispatch table entry for balanceOf(address)
            var1 = msg.value;
        
            if (var1) { revert(memory[0x00:0x00]); }
        
            var1 = 0x013a;
            var2 = msg.data[0x04:0x24] & 0xffffffffffffffffffffffffffffffffffffffff;
            var2 = balanceOf(var2);
        
        label_013A:
            var temp3 = memory[0x40:0x60];
            memory[temp3:temp3 + 0x20] = var2;
            var temp4 = memory[0x40:0x60];
            return memory[temp4:temp4 + temp3 - temp4 + 0x20];
        } else if (var0 == 0x7ce7c990) {
            // Dispatch table entry for transfer2(address,uint256)
            var1 = msg.value;
        
            if (var1) { revert(memory[0x00:0x00]); }
        
            var1 = 0x009c;
            var2 = msg.data[0x04:0x24] & 0xffffffffffffffffffffffffffffffffffffffff;
            var var3 = msg.data[0x24:0x44];
            transfer2(var2, var3);
            stop();
        } else if (var0 == 0xa9059cbb) {
            // Dispatch table entry for transfer(address,uint256)
            var1 = msg.value;
        
            if (var1) { revert(memory[0x00:0x00]); }
        
            var1 = 0x009c;
            var2 = msg.data[0x04:0x24] & 0xffffffffffffffffffffffffffffffffffffffff;
            var3 = msg.data[0x24:0x44];
            transfer(var2, var3);
            stop();
        } else if (var0 == 0xcbfc4bce) {
            // Dispatch table entry for 0xcbfc4bce (gift(address))
            var1 = msg.value;
        
            if (var1) { revert(memory[0x00:0x00]); }
        
            var1 = 0x013a;
            var2 = msg.data[0x04:0x24] & 0xffffffffffffffffffffffffffffffffffffffff;
            var2 = func_0417(var2);
            goto label_013A;
        } else { revert(memory[0x00:0x00]); }
    }
    
    function func_01DC() {
        memory[0x00:0x20] = msg.sender;
        memory[0x20:0x40] = 0x01;
    
        if (storage[keccak256(memory[0x00:0x40])]) { revert(memory[0x00:0x00]); }
    
        memory[0x00:0x20] = msg.sender;
        memory[0x20:0x40] = 0x00;
        var temp0 = keccak256(memory[0x00:0x40]);
        storage[temp0] = storage[temp0] + 0x01;
        memory[0x20:0x40] = 0x01;
        storage[keccak256(memory[0x00:0x40])] = 0x01;
    }
    
    function profit() {
        memory[0x00:0x20] = msg.sender;
        memory[0x20:0x40] = 0x00;
    
        if (storage[keccak256(memory[0x00:0x40])] != 0x01) { revert(memory[0x00:0x00]); }
    
        memory[0x00:0x20] = msg.sender;
        memory[0x20:0x40] = 0x01;
    
        if (storage[keccak256(memory[0x00:0x40])] != 0x01) { revert(memory[0x00:0x00]); }
    
        memory[0x00:0x20] = msg.sender;
        memory[0x20:0x40] = 0x00;
        var temp0 = keccak256(memory[0x00:0x40]);var temp0 = keccak256(memory[0x00:0x40]);
        storage[temp0] = storage[temp0] + 0x01;
        memory[0x20:0x40] = 0x01;
        storage[keccak256(memory[0x00:0x40])] = 0x02;
    }
    
    function func_0278(var arg0) {
        memory[0x00:0x20] = msg.sender;
        memory[0x20:0x40] = 0x00;
    
        if (0x2710 > balanceOf[msg.sender]) { revert(memory[0x00:0x00]); }
    
        var var0 = 0xb1bc9a9c599feac73a94c3ba415fa0b75cbe44496bfda818a9b4a689efb7adba;
        var var1 = 0x01;
        var temp0 = arg0;
        var var2 = temp0;
        var temp1 = memory[0x40:0x60];
        var var3 = temp1;
        memory[var3:var3 + 0x20] = var1;
        var temp2 = var3 + 0x20;
        var var4 = temp2;
        var temp3 = var4 + 0x20;
        memory[var4:var4 + 0x20] = temp3 - var3;
        memory[temp3:temp3 + 0x20] = memory[var2:var2 + 0x20];
        var var5 = temp3 + 0x20;
        var var7 = memory[var2:var2 + 0x20];
        var var6 = var2 + 0x20;
        var var8 = var7;
        var var9 = var5;
        var var10 = var6;
        var var11 = 0x00;
    
        if (var11 >= var8) {
        label_02FD:
            var temp4 = var7;
            var5 = temp4 + var5;
            var6 = temp4 & 0x1f;
        
            if (!var6) {
                var temp5 = memory[0x40:0x60];
                log(memory[temp5:temp5 + var5 - temp5], [stack[-7]]);
                return;
            } else {
                var temp6 = var6;
                var temp7 = var5 - temp6;
                memory[temp7:temp7 + 0x20] = ~(0x0100 ** (0x20 - temp6) - 0x01) & memory[temp7:temp7 + 0x20];
                var temp8 = memory[0x40:0x60];
                log(memory[temp8:temp8 + (temp7 + 0x20) - temp8], [stack[-7]]);
                return;
            }
        } else {
        label_02EE:
            var temp9 = var11;
            memory[temp9 + var9:temp9 + var9 + 0x20] = memory[temp9 + var10:temp9 + var10 + 0x20];
            var11 = temp9 + 0x20;
        
            if (var11 >= var8) { goto label_02FD; }
            else { goto label_02EE; }
        }
    }
    
    function balanceOf(var arg0) returns (var arg0) {
        memory[0x20:0x40] = 0x00;
        memory[0x00:0x20] = arg0;
        return storage[keccak256(memory[0x00:0x40])];
    }
    
    function transfer2(var arg0, var arg1) {
        if (arg1 <= 0x02) { revert(memory[0x00:0x00]); }
    
        memory[0x00:0x20] = msg.sender;
        memory[0x20:0x40] = 0x00;
    
        if (0x02 >= storage[keccak256(memory[0x00:0x40])]) { revert(memory[0x00:0x00]); }
    
        memory[0x00:0x20] = msg.sender;
        memory[0x20:0x40] = 0x00;
    
        if (storage[keccak256(memory[0x00:0x40])] - arg1 <= 0x00) { revert(memory[0x00:0x00]); }
    
        memory[0x00:0x20] = msg.sender;
        memory[0x20:0x40] = 0x00;
        var temp0 = keccak256(memory[0x00:0x40]);
        var temp1 = arg1;
        storage[temp0] = storage[temp0] - temp1;
        memory[0x00:0x20] = arg0 & 0xffffffffffffffffffffffffffffffffffffffff;
        var temp2 = keccak256(memory[0x00:0x40]);
        storage[temp2] = temp1 + storage[temp2];
    }
    
    function transfer(var arg0, var arg1) {
        if (arg1 <= 0x01) { revert(memory[0x00:0x00]); }
    
        memory[0x00:0x20] = msg.sender;
        memory[0x20:0x40] = 0x00;
    
        if (0x01 >= storage[keccak256(memory[0x00:0x40])]) { revert(memory[0x00:0x00]); }
    
        memory[0x00:0x20] = msg.sender;
        memory[0x20:0x40] = 0x00;
    
        if (arg1 > storage[keccak256(memory[0x00:0x40])]) { revert(memory[0x00:0x00]); }
    
        memory[0x00:0x20] = msg.sender;
        memory[0x20:0x40] = 0x00;
        var temp0 = keccak256(memory[0x00:0x40]);
        var temp1 = arg1;
        storage[temp0] = storage[temp0] - temp1;
        memory[0x00:0x20] = arg0 & 0xffffffffffffffffffffffffffffffffffffffff;
        var temp2 = keccak256(memory[0x00:0x40]);
        storage[temp2] = temp1 + storage[temp2];
    }
    
    function func_0417(var arg0) returns (var arg0) {
        memory[0x20:0x40] = 0x01;
        memory[0x00:0x20] = arg0;
        return storage[keccak256(memory[0x00:0x40])];
    }
}
```

### 翻译成solidity

```js
pragma solidity ^0.4.24;

contract DaysBank {
    mapping(address => uint) public balanceOf;
    mapping(address => uint) public gift;
    address owner;
        
    constructor()public{
        owner = msg.sender;
    }
    
    event SendFlag(uint256 flagnum, string b64email);

    function payforflag(string b64email) public {

        require(balanceOf[msg.sender] >= 10000);

        emit SendFlag(1,b64email);

    }

    function transfer2(var address_in, var money) {
            require(money > 0x02)
            require(balanceOf[msg.sender] > 0x02)
            require(balanceOf[msg.sender] - money > 0x00)

            balanceOf[msg.sender] -=  money;
            balanceOf[address_in] += money;
    }
    function transfer(var address_in, var money) {
            require(money > 0x01)
            require(balanceOf[msg.sender] > 0x01)
            require(balanceOf[msg.sender] >= money)

            balanceOf[msg.sender] -=  money;
            balanceOf[address_in] += money;
    }
    function profit() {
        require(balanceOf[msg.sender] == 0x01)
        require(gift[msg.sender] == 0x01)
        balanceOf[msg.sender] += 1
        gift[msg.sender] = 0x02
    }

    function func_01DC() {

        require(gift[msg.sender] == 0x00)

        balanceOf(msg.sender) += 0x01

        gift[msg.sender] = 0x01
    }
}
```

### 漏洞

require(balanceOf[msg.sender] - money > 0x00)
transfer2函数存在溢出漏洞

### 操作步骤

+ 第一步 获取gift
web3.eth.sendTransaction({to: "0x455541c3e9179a6cd8C418142855d894e11A288c",data:'0x652e9d91'})
+ 第二步 调用profit()
    balance=2 gift=2
+ 第三步 换一个账号重复以上两步
+ 第四步 调用transfer第一个账号给第二个账号转2块钱
    第二个账号balance=4 gift=2
+ 第五步 调用transfer2第二个账号给第一个账号转9999999999999999999999999999块钱
    第二个账号balance溢出 超级大
+ 第六步 调用payforflag 传入邮箱base64
+ 邮箱获取flag

## FLAG值

![](flag.png)

