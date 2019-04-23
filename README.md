# pwnable.tw_babystack  

strcmp가 널바이트까지만 체크를 한다는 점을 이용해준다  
한바이트씩 브루트포싱으로 랜덤넘버를 알아낼 수 있으며, libc릭도 가능하다.  
libc릭 같은 경우, 정말 어이없게도 ubuntu 18.04에서는 불가능했지만, 16.04에서는 스택에서의 구조상 가능했다.  
strcpy를 이용해서 스택 버퍼오버플로우를 일으켜 return address를 one_gadget으로 덮어 clear!  

서버가 상당히 느리고 입출력을 제대로 받지를 못해 애먹었다..  
