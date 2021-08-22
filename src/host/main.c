#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void *threadInterface(void *args)
{
  int returnValue = system("python3 ../interface/rfid-interface.py");
}

void *threadServer(void *args)
{
  int returnValue = system("node ../server/app.js");
}

int main(void)
{
  pthread_t interface_thread_id;
  pthread_t server_thread_id;

  pthread_create(&interface_thread_id, NULL, threadInterface, NULL);
  pthread_join(interface_thread_id, NULL);

  pthread_create(&server_thread_id, NULL, threadServer, NULL);
  pthread_join(server_thread_id, NULL);

  return 0;
}