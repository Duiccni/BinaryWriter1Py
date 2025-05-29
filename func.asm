bits 64

; C:\Users\abi37\AppData\Local\bin\NASM\nasm.exe func.asm -o func.bin -f bin

lea rdx, [rel msg]
jmp rax

msg: db "i love big cocks :3", 0