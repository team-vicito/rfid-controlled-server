#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <pthread.h>

pthread_t server_thread_id;
pthread_t interface_thread_id;

void *threadServer(void *args)
{
  int returnValue = system("node ./src/server/app.js");
}

void *threadInterface(void *args)
{
  int returnValue = system("python3 ./src/interface/rfid-interface.py");
}

void sigHandler(int _) {
  pthread_cancel(server_thread_id);
  pthread_cancel(interface_thread_id);
}

int main(void)
{
  signal(SIGINT, sigHandler);
  signal(SIGTERM, sigHandler);

  pthread_create(&server_thread_id, NULL, threadServer, NULL);
  pthread_create(&interface_thread_id, NULL, threadInterface, NULL);

  pthread_join(server_thread_id, NULL);
  pthread_join(interface_thread_id, NULL);

  return 0;
}