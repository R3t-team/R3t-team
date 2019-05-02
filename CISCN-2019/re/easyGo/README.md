用[IDA插件](https://github.com/sibears/IDAGolangHelper)可以显示symbol，逆起来更清楚。可以看到有一个base64加密。

```c
__int64 __fastcall main_main(__int64 a1, __int64 a2)
{
  __int64 v2; // r8
  __int64 v3; // r9
  __int64 v4; // r8
  __int64 v5; // r9
  __int64 v6; // rdx
  __int64 v7; // rcx
  __int64 v8; // r8
  __int64 v9; // r9
  __int128 v10; // ST00_16
  __int64 v11; // ST18_8
  int v12; // er8
  __int64 v13; // r8
  __int64 v14; // r9
  __int64 result; // rax
  __int64 v16; // rdx
  __int64 v17; // r8
  __int64 v18; // r9
  __int64 v19; // rdx
  __int64 v20; // r8
  __int64 v21; // r9
  __int64 v22; // r8
  __int64 v23; // r9
  __int64 v24; // [rsp+8h] [rbp-F8h]
  char v25; // [rsp+58h] [rbp-A8h]
  char v26; // [rsp+80h] [rbp-80h]
  __int64 v27; // [rsp+98h] [rbp-68h]
  __int64 v28; // [rsp+A0h] [rbp-60h]
  __int128 v29; // [rsp+A8h] [rbp-58h]
  __int128 v30; // [rsp+B8h] [rbp-48h]
  __int128 v31; // [rsp+C8h] [rbp-38h]
  __int128 v32; // [rsp+D8h] [rbp-28h]
  __int128 v33; // [rsp+E8h] [rbp-18h]

  if ( (unsigned __int64)&v26 <= *(_QWORD *)(__readfsqword(0xFFFFFFF8) + 16) )
    runtime_morestack_noctxt(a1, a2);
  runtime_newobject(a1, a2);
  v28 = v24;
  *(_QWORD *)&v33 = &string_autogen_4MIYT3;
  *((_QWORD *)&v33 + 1) = &intro;
  fmt_Fprintln(a1, a2, (__int64)&v33, (__int64)&string_autogen_4MIYT3, v2, v3, (__int64)&enc, qword_572B18);
  *(_QWORD *)&v32 = &ptr_string;
  *((_QWORD *)&v32 + 1) = v28;
  fmt_Fscanf(
    a1,
    a2,
    (__int64)&off_4E2880,
    (__int64)&v32,
    v4,
    v5,
    (__int64)&off_4E2880,
    qword_572B10,
    (__int64)&unk_4C8569,
    2LL);
  runtime_stringtoslicebyte(a1, a2, v6, v7, v8, v9);
  *(_QWORD *)&v10 = &v25;
  *((_QWORD *)&v10 + 1) = v11;
  runtime_slicebytetostring(a1, a2, v11, 1, v12, v10);
  encoding_base64__ptr_Encoding_DecodeString(a1, a2, 1LL, (__int64)&v32, v13, v14, qword_572B00, (__int64)&v32);
  v27 = 1LL;
  MEMORY[0x19](a1);
  runtime_convTstring(a1, a2, v19);
  *(_QWORD *)&v31 = &string_autogen_4MIYT3;
  *((_QWORD *)&v31 + 1) = 1LL;
  fmt_Fprintln(a1, a2, (__int64)&enc, (__int64)&string_autogen_4MIYT3, v20, v21, (__int64)&enc, qword_572B18);
  if ( *(__int128 **)(v28 + 8) == &v32 )
  {
    runtime_memequal(a1, a2, v27, *(_QWORD *)v28);
    *(_QWORD *)&v30 = &string_autogen_4MIYT3;
    *((_QWORD *)&v30 + 1) = &success;
    result = fmt_Fprintln(a1, a2, v16, (__int64)&enc, v17, v18, (__int64)&enc, qword_572B18);
  }
  else
  {
    *(_QWORD *)&v29 = &string_autogen_4MIYT3;
    *((_QWORD *)&v29 + 1) = &fail;
    result = fmt_Fprintln(a1, a2, v27, (__int64)&enc, v22, v23, (__int64)&enc, qword_572B18);
  }
  return result;
}
```

gdb下断点到`base64`这里。

```
assassinq>> searchmem flag
Searching for 'flag' in: None ranges
Found 29 results, display max 29 items:
easyGo : 0x496569 --> 0x6604000067616c66 
easyGo : 0x497073 --> 0x500007367616c66 
easyGo : 0x4972d4 --> 0x7405000067616c66 
easyGo : 0x4977a8 --> 0x600007367616c66 
easyGo : 0x497c09 --> 0x700007367616c66 
easyGo : 0x498639 --> 0x800007367616c66 
easyGo : 0x498720 --> 0x800007367616c66 
easyGo : 0x49881d --> 0x800007367616c66 
easyGo : 0x4992b8 --> 0xa00007367616c66 ('flags')
easyGo : 0x49c2ec --> 0x2a0d000067616c66 ('flag')
easyGo : 0x49c629 --> 0x2a0e000167616c66 
easyGo : 0x49c74a --> 0x2a0e000067616c66 
easyGo : 0x4b095c ("flags int32; fd int32; off uint32; ret *uintptr }")
easyGo : 0x4c8bb2 ("flags rip    rsi    rsp    runningsignal syscalluintptrunknownwaiting etypes  goal\316\224= is not  mcount= minutes nalloc= newval= nfreed= packed= pointer stack=[ status , idle: 0123456748828125ArmenianBal"...)
easyGo : 0x4cee90 ("flag you input is correct!cannot send after transport endpoint shutdownexitsyscall: syscall frame is no longer validheapBitsSetType: called with non-pointer typereflect: internal error: invalid method"...)
easyGo : 0x4cefc9 ("flag like flag{123} to judge:memory reservation exceeds address space limitpanicwrap: unexpected string after type name: reflect.Value.Slice: slice index out of boundsreflect: nil type passed to Type."...)
easyGo : 0x4cefd3 ("flag{123} to judge:memory reservation exceeds address space limitpanicwrap: unexpected string after type name: reflect.Value.Slice: slice index out of boundsreflect: nil type passed to Type.Convertibl"...)
easyGo : 0x4cf95c ("flagruntime:stoplockedm: g is not Grunnable or Gscanrunnable\nruntime: mmap: too much locked memory (check 'ulimit -l').\nsync/atomic: store of inconsistently typed value into Valueruntime: may need to "...)
easyGo : 0x51552d --> 0x7200007367616c66 ('flags')
easyGo : 0x53c6e0 ("flag.mustBe")
easyGo : 0x53c6f5 ("flag.kind")
easyGo : 0x53c7c0 ("flag.mustBeExported")
easyGo : 0x53c8a8 ("flag.mustBeAssignable")
easyGo : 0x53cf79 --> 0x6f722e67616c66 ('flag.ro')
--More--(25/30)
easyGo : 0x5559a9 --> 0x200007367616c66 
easyGo : 0x55e3a6 ("flags_amd64.go")
mapped : 0xc000076041 ("flag like flag{123} to judge:\n")
mapped : 0xc00007604b ("flag{123} to judge:\n")
mapped : 0xc000076060 ("flag{92094daf-33c9-431e-a85a-8bfbd5df98ad}")
```

随手`searchmem`以下，在内存里就看到了flag。
