#include "stdio.h"

class CL_name;

/**
 * @brief Just a comment
 * @real{REQ-0015}
 * @real{REQ-003302,02}
 */
class CL_main : public basicStuff{
public:
    enum enumName{
        Value1 = 2,
        Value2 = 3
    };
    CL_main();
    ~CL_main();

    virtual void met1(const uint8 mm);
private:
    /**
     * @brief Just a comment
     * @real{REQ-0015}
     */
    struct structName{
        int value;
        /// @real{REQ-Struct-Attr_kkk}
        char kkkkk;
    };
    /**
     * @brief Just a comment
     * @real{REQ-0805}
     */
    class CL_insideClass{
        /**
         * @brief Just a comment
         * @real{REQ-0005}
         */
        virtual void insideClassMethod1 (int param1);
    };
    /// @real{REQ-Attr_01}
    int mAttribute1;
    /// @real{REQ-Attr_02}
    Class<2, 3> mAttribute2;
};

int main(int argc, void **argv){
    return 1;
}

class CL_main2{
public:
        /// @real{REQ-CL_main2-constructor}
        CL_main2();    
};

struct ST_main{
public:
    /**
     * @brief Just a comment
     * @real{ASD-0003-01}
     * REQ-0003-01asdasdasdasdasdasd
     */
    ~ST_main();   

}