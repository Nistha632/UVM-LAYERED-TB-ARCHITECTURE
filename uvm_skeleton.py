print("------------------------------------------------------------------------")
project = input("name of the project = ")
print("------------------------------------------------------------------------")
if(not(project and project.strip())):
    print("please insert proper name")
else:
    if(project[0].isnumeric()):
        print("first character should not be numeric")
    else:
        while(1):
            #print("------------------------------------------------------------------------")
            print("enter 1 --->  for testbench file")
            print("enter 2 --->  for test class ")
            print("enter 3 --->  for env class")
            print("enter 4 --->  for agent class")
            print("enter 5 --->  for driver class")
            print("enter 6 --->  for monitor class")
            print("enter 7 --->  for sequencer class")
            print("enter 8 --->  for interface class")
            print("enter 9 --->  for sequence class")
            print("enter 10 --->  for sequence item class")
            print("enter 11 --->  for scoreboard class")
            print("enter 12 --->  for coverage class")
            print("enter all --->  for all class")
            print("enter exit  ---> to exit the code")
            print("------------------------------------------------------------------------")
            select = input("select input to create class\n")
            print("------------------------------------------------------------------------")
            if select == "exit":
                break

            if(select == "1" or select == "all"):
                f = open("testbench.sv","w+")
                f.write("import uvm_pkg::*;\n\
    `include \""+project+"_interface.sv\"\n\
    `include \""+project+"_sequence_item.sv\"\n\
    `include \""+project+"_sequence.sv\"\n\
    `include \""+project+"_driver.sv\"\n\
    `include \""+project+"_monitor.sv\"\n\
    `include \""+project+"_sequencer.sv\"\n\
    `include \""+project+"_coverage.sv\"\n\
    `include \""+project+"_scoreboard.sv\"\n\
    `include \""+project+"_agent.sv\"\n\
    `include \""+project+"_env.sv\"\n\
    `include \""+project+"_test.sv\"\n\
    module "+project+"_tb;\n\
    bit clk;\n\
    bit reset;\n\
    \n\
    "+project+"_pif pif(clk,reset);\\ interface \n\
    \n\
    initial begin \n\
         $dumpfile(\""+project+".vcd\");\n\
         $dumpvars;\n\
    end\n\
    // reset logic\n\
    initial begin \n\
         reset = 1;\n\
         @(posedge clk)\n\
         reset = 0;\n\
         @(posedge clk)\n\
         @(posedge clk)\n\
         reset = 1;\n\
    end\n\
    // clock generation\n\
    always #10 clk = ~clk; \n\
    initial begin\n\
            `uvm_info(\"test top\",\"config db\",UVM_LOW)\n\
            uvm_config_db #(virtual "+project+"_pif) :: set(uvm_root::get(),\"\")\n\
            run_test();\n\
    end\n\
    endmodule : "+project+"_tb")
                f.close()
                print("---> testbench file created");

                if(select == "2" or select == "all"):
                    f = open(""+project+"_test.sv","w+")
                    f.write("class "+project+"_test extends uvm_test;\n\
    "+project+"_env env;\n\
    virtual "+project+"_pif vif;\n\
    `uvm_component_utils("+project+"_test)\n\
    function new(string name, uvm_component parent);\n\
         super.new(name,parent);\n\
         `uvm_info(\""+project+"_test\",\"new construtor called\", UVM_LOW)\n\
    endfunction : new\n\
    \n\
    function void build_phase(uvm_phase phase);\n\
        super.build_phase(phase);\n\
        `uvm_info(\""+project+"_test\",\"build phase\", UVM_LOW)\n\
        \n\
        env = "+project+"_env::type_id::create(\"env\",this);\n\
        \n\
        if(!uvm_config_db#(virtual "+project+"_pif::get(this,\"env\",\"vif\",vif)))\n\
        `uvm_error(\"build_phase\",\"test virtual interface failed\")\n\
        end\n\
        uvm_config_db#(virtual "+project+"_pif::get(this,\"env\",\"vif\",vif)))\n\
    endfunction\n\
    \n\
    \n\
    endclass : "+project+"_test")
                    f.close()
                    print("---> test file created")

                if(select == "3" or select == "all"):
                    f = open(""+project+"_env.sv","w+")
                    f.write("class "+project+"_env extends uvm_env;\n\
    "+project+"_agent agt;\n\
    "+project+"_coverage cvr;\n\
    "+project+"_scoreboard scb\n\
    virtual "+project+"_pif vif;\n\
    `uvm_component_utils("+project+"_env)\n\
    \n\
    function new(string name, uvm_component parent);\n\
        super.new(name,parent);\n\
        `uvm_info(\""+project+"_env\",\"new construtor called\", UVM_LOW)\n\
    endfunction : new\n\
    \n\
    function void build_phase(uvm_phase phase);\n\
        super.build_phase(phase);\n\
        `uvm_info(\""+project+"_env\",\"build phase\", UVM_LOW)\n\
        \n\
        agt = "+project+"_agent::type_id::create(\"agt\",this);\n\
        cvr = "+project+"_coverage::type_id::create(\"cvr\",this);\n\
        scb = "+project+"_scoreboard::type_id::create(\"scb\",this);\n\
        \n\
        if(!uvm_config_db#(virtual "+project+"_pif::get(this,\"env\",\"vif\",vif)))\n\
            `uvm_fatal(\"build_phase\",\"no virtual interface specified\")\n\
        end\n\
        uvm_config_db#(virtual "+project+"_pif::get(this,\"env\",\"vif\",vif)))\n\
    endfunction\n\
    \n\
    function void connect_phase(uvm_phase phase);\n\
        super.connect_phase(phase);\n\
        `uvm_info(\""+project+"_env\",\"connect phase\", UVM_LOW)\n\
        agt.mon.ap_mon.connect(cvr.analysis export);\n\
        agt.mon.ap_mon.connect(scb.ap_imp);\n\
    endfunction\n\
    \n\
    endclass : "+project+"_env")
                    f.close();
                    print("---> env file created");

                if(select == "4" or select == "all"):
                    f = open(""+project+"_agent.sv","w+")
                    f.write("class "+project+"_agent extends uvm_agent;\n\
    "+project+"_mon mon;\n\
    "+project+"_drv drv;\n\
    "+project+"_seqr seqr\n\
    virtual "+project+"_pif vif;\n\
    `uvm_component_utils_begin("+project+"_agent)\n\
    `uvm_field_object(mon,UVM_ALL_ON);\n\
    `uvm_field_object(drv,UVM_ALL_ON);\n\
    `uvm_field_object(seqr,UVM_ALL_ON);\n\
    `uvm_component_utils_end\n\
    \n\
    function new(string name, uvm_component parent);\n\
        super.new(name,parent);\n\
        `uvm_info(\""+project+"_agent\",\"new construtor called\", UVM_LOW)\n\
    endfunction : new\n\
    \n\
    function void build_phase(uvm_phase phase);\n\
        super.build_phase(phase);\n\
        `uvm_info(\""+project+"_agent\",\"build phase\", UVM_LOW)\n\
        \n\
        mon = "+project+"_mon::type_id::create(\"mon\",this);\n\
        drv = "+project+"_drv::type_id::create(\"drv\",this);\n\
        seqr = "+project+"_seqr::type_id::create(\"seqr\",this);\n\
        \n\
        if(!uvm_config_db#(virtual "+project+"_pif::get(this,\"env\",\"vif\",vif)))\n\
            `uvm_fatal(\"build_phase\",\"no virtual interface specified\")\n\
            end\n\
        uvm_config_db#(virtual "+project+"_pif::get(this,\"seqr\",\"vif\",vif)))\n\
        uvm_config_db#(virtual "+project+"_pif::get(this,\"drv\",\"vif\",vif)))\n\
        uvm_config_db#(virtual "+project+"_pif::get(this,\"mon\",\"vif\",vif)))\n\
    endfunction\n\
    \n\
    function void connect_phase(uvm_phase phase);\n\
        super.connect_phase(phase);\n\
        `uvm_info(\""+project+"_agent\",\"connect phase\", UVM_LOW)\n\
        drv.seq_item_port.connect(seqr.seq_item_export);\n\
    endfunction\n\
    \n\
    endclass : "+project+"_agent")
                    f.close();
                    print("---> agent file created");

                if(select == "5" or select == "all"):
                    f = open(""+project+"_driver.sv","w+")
                    f.write("define inf vif."+project+"_drv_mp."+project+"_drv_clk\n\
    class "+project+"_drv extends uvm_driver#("+project+"_seq_item;\n\
    "+project+"_seq_item seq_item;\n\
    virtual "+project+"_pif vif;\n\
    `uvm_component_utils_begin("+project+"_drv)\n\
    \n\
    function new(string name, uvm_component parent);\n\
        super.new(name,parent);\n\
        `uvm_info(\""+project+"_drv\",\"new construtor called\", UVM_LOW)\n\
    endfunction : new\n\
    \n\
    function void build_phase(uvm_phase phase);\n\
        super.build_phase(phase);\n\
        `uvm_info(\""+project+"_driver\",\"build phase\", UVM_LOW)\n\
        \n\
        if(!uvm_config_db#(virtual "+project+"_pif::get(this,\"env\",\"vif\",vif)))\n\
           `uvm_fatal(\"build_phase\",\"no vif\")\n\
        end\n\
    endfunction\n\
    \n\
    virtual task run_phase(uvm_phase phase);\n\
       super.run_phase(phase);\n\
       `uvm_info(\""+project+"_driver\",\"run phase\", UVM_LOW)\n\
    endtask\n\
    \n\
    endclass : "+project+"_driver")
                    f.close();
                    print("---> driver file created");

                if(select == "6" or select == "all"):
                    f = open(""+project+"_monitor.sv","w+")
                    f.write("define inf vif."+project+"_mon_mp."+project+"_mon_clk\n\
    class "+project+"_mon extends uvm_monitor#("+project+"_seq_item;\n\
    "+project+"_seq_item seq_item;\n\
    virtual "+project+"_pif vif;\n\
    `uvm_component_utils_begin("+project+"_mon)\n\
    \n\
    uvm_analysis_port#("+project+"_seq_item) ap_mon;\n\
    function new(string name, uvm_component parent);\n\
        super.new(name,parent);\n\
        `uvm_info(\""+project+"_mon\",\"new construtor called\", UVM_LOW)\n\
    endfunction : new\n\
    \n\
    function void build_phase(uvm_phase phase);\n\
        super.build_phase(phase);\n\
        `uvm_info(\""+project+"_monitor\",\"build phase\", UVM_LOW)\n\
        \n\
        if(!uvm_config_db#(virtual "+project+"_pif::get(this,\"env\",\"vif\",vif)))\n\
           `uvm_fatal(\"build_phase\",\"no vif\")\n\
        end\n\
        ap_mon = new(\"ap_mon\",this);\n\
        seq_item = "+project+"_seq_item::type_id::create(\"tx\",this);\n\
    endfunction\n\
    \n\
    virtual task run_phase(uvm_phase phase);\n\
        ap_mon.write(seq_item);\n\
        uvm_info(\""+project+"_monitor\",\"run phase\", UVM_LOW)\n\
    endtask\n\
    \n\
    endclass : monitor")
                    f.close();
                    print("---> monitor file created");

                if(select == "7" or select == "all"):
                    f = open(""+project+"_sequencer.sv","w+")
                    f.write("class "+project+"_seqr extends uvm_sequencer#("+project+"_seq_item;\n\
    `uvm_component_utils_begin("+project+"_seqr)\n\
    \n\
    function new(string name, uvm_component parent);\n\
        super.new(name,parent);\n\
        `uvm_info(\""+project+"_seqr\",\"new construtor called\", UVM_LOW)\n\
    endfunction : new\n\
    \n\
    function void build_phase(uvm_phase phase);\n\
        super.build_phase(phase);\n\
        `uvm_info(\""+project+"_sequencer\",\"build phase\", UVM_LOW)\n\
    endfunction\n\
    \n\
    endclass : "+project+"_sequencer")
                    f.close();
                    print("---> sequencer file created");

                if(select == "8" or select == "all"):
                    f = open(""+project+"_interface.sv","w+")
                    f.write("interface "+project+"_pif #(parameter );\n\
    \n\
    clocking "+project+"_drv_clk @(posedge clk);\n\
       default input #1 output #1;\n\
    endclocking : "+project+"_drv_clk\n\
    \n\
    clocking "+project+"_mon_clk @(posedge clk);\n\
       default input #1 output #1;\n\
    endclocking : "+project+"_mon_clk\n\
    \n\
    clocking "+project+"_dut_clk @(posedge clk);\n\
       default input #1 output #1;\n\
    endclocking : "+project+"_dut_clk\n\
    \n\
    modport "+project+"_mon_mp(clocking "+project+"_mon_clk,input clk, reset);\n\
    modport "+project+"_dut_mp(clocking "+project+"_dut_clk,input clk, reset);\n\
    modport "+project+"_drv_mp(clocking "+project+"_drv_clk,input clk, reset);\n\
    endclass : "+project+"_pif")
                    f.close();
                    print("---> interface file created");

                if(select == "9" or select == "all"):
                    f = open(""+project+"_sequence.sv","w+")
                    f.write("class "+project+"_test extends uvm_sequence#("+project+"_seq_item;\n\
    `uvm_object_utils("+project+"_sequence)\n\
    \n\
    function new(string name, uvm_component parent);\n\
        super.new(name,parent);\n\
        `uvm_info(\""+project+"_sequence\",\"new construtor called\", UVM_LOW)\n\
    endfunction : new\n\
    \n\
    task body();\n\
        int addr_que[$];\n\
        "+project+"_seq_item seq_item;\n\
        `uvm_info(\""+project+"_sequence\",\"body task\", UVM_LOW)\n\
    endtask\n\
    endclass : "+project+"_sequencer")
                    f.close();
                    print("---> sequence file created");

                if(select == "10" or select == "all"):
                    f = open(""+project+"_seq_item.sv","w+")
                    f.write("class "+project+"_seq_item extends uvm_sequence_item;\n\
    `uvm_object_utils("+project+"_seq_item)\n\
    \n\
    function new(string name, uvm_component parent);\n\
        super.new(name,parent);\n\
        `uvm_info(\""+project+"_seq_item\",\"new construtor called\", UVM_LOW)\n\
    endfunction : new\n\
    \n\
    endclass : "+project+"_seq_item")
                    f.close();
                    print("---> seq item file created");

             
                if(select == "11" or select == "all"):
                    f = open(""+project+"_scoreboard.sv","w+")
                    f.write("class "+project+"_scoreboard extends uvm_scoreboard;\n\
    `uvm_component_utils_begin("+project+"_scoreboard)\n\
    \n\
    "+project+"_seq_item seq_item_que[$];\n\
    uvm_analysis_imp#("+project+"_seq_item,"+project+"_scoreboard)ap_imp;\n\
    function new(string name, uvm_component parent);\n\
        super.new(name,parent);\n\
        ap_imp = new(\"ap_imp\",this);\n\
        `uvm_info(\""+project+"_scoreboard\",\"new construtor called\", UVM_LOW)\n\
    endfunction : new\n\
    \n\
    function void build_phase(uvm_phase phase);\n\
        super.build_phase(phase);\n\
    endfunction\n\
    \n\
    function void write("+project+"_seq_item seq_item);\n\
    endfunction\n\
   \n\
    virtual task run_phase(uvm_phase phase);\n\
    endtask\n\
    \n\
    endclass : "+project+"_scoreboard")
                    f.close();
                    print("---> scoreboard file created");

                if(select == "12" or select == "all"):
                    f = open(""+project+"_coverage.sv","w+")
                    f.write("class "+project+"_coverage extends uvm_subscriber#("+project+"_seq_item;\n\
    `uvm_component_utils_begin("+project+"_covergae)\n\
    \n\
    virtual "+project+"_pif vif;\n\
    "+project+"_seq_items seq_item;\n\
    real cov;\n\
    \n\
    function new(string name, uvm_component parent);\n\
        super.new(name,parent);\n\
        `uvm_info(\""+project+"_coverage\",\"new construtor called\", UVM_LOW)\n\
    endfunction : new\n\
    \n\
    function void build_phase(uvm_phase phase);\n\
        super.build_phase(phase);\n\
        uvm_config_db#(virtual "+project+"_pif)::get(this,\"env\",\"vif\",vif)\n\
    endfunction\n\
    \n\
    function void write("+project+"_seq_item seq_item);\n\
    endfunction\n\
    \n\
    function void extract_phase(uvm_phase phase);\n\
    endfunction\n\
   \n\
    function void report_phase(uvm_phase phase);\n\
    endfunction\n\
   \n\
    endclass : "+project+"_coverage")
                    f.close();
                    print("---> coverage file created");

                    if(select != "all"):
                            yesno = input("want to create any more files?(y/n)")
                            if(yesno == "n"):
                               break
                            else:
                               break

