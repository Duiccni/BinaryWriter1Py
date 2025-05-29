bits 64

; C:\Users\abi37\AppData\Local\bin\NASM\nasm.exe main.asm -o main.bin -f bin

sub rsp, 0x28

xor rcx, rcx
mov r9, rcx
lea rdx, [rel title]
lea r8, [rel title]
mov rax, [rel $-($-$$)+0x268]
call [rel $-($-$$)+0x278]

xor ecx, ecx
call [rel $-($-$$)+0x258]
mov ecx, eax
call [rel $-($-$$)+0x250]

title: db "test", 0