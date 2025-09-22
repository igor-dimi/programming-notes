#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char const *argv[])
{
    // Open a file using hte system call wrapper open()
    int fd = open("demo.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd == -1) {
        perror("open");
        return 1;
    }
    printf("file descriptor from open(): %d\n", fd);
    // comment
    // another comment
    const char *msg = "hello via write()\n";
    write(fd, msg, 18);

    // now wrap the same fd in a c standard library FILE*
    FILE *fp = fdopen(fd, "w");
    if (!fp) {
        perror("fdopen");
        return 1;
    }

    // use buffered stdio

    fprintf(fp, "hello via fprintf()\n");

    // fflush ensures buffer is written out
    fflush(fp);

    // fclose will also close the underlying fd

    fclose(fp);
    return 0;
}