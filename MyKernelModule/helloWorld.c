#include<linux/module.h>
#include<linux/kernel.h>
#include<linux/init.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Sanjeev A");
MODULE_DESCRIPTION("Hello world program");

static int __init hello_init(void){
    printk(KERN_INFO "Hello world\n");
    return 0;
}

static void __exit hello_exit(void){
    printk(KERN_INFO "Exiting\n");
    return;
}

module_init(hello_init);
module_exit(hello_exit);