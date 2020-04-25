

    public static void main(String[] args) throws Exception{
        DictWithMultiLable tree = new DictWithMultiLable();
        tree.initSearchParm("F:\\dict.txt"); //初始化词典（歌曲相声等标签）
        long t1 = System.currentTimeMillis();
        Map<String, Set<String>> res = tree.dicMatch("沙漠骆驼");//查找
        long t2 = System.currentTimeMillis();
        System.out.println(res);
        System.out.println("search cose time : " + (t2-t1));
//        gene_line_entity_pair(tree);
    }

    static TreeNode head = new TreeNode(); //树的根节点
    static int maxWordLen = 0; //最大的单词长度
    static Set<String> allWord = new HashSet<String>();  //所有的单词的缓存
    static TreeNode endNode = new TreeNode("<eos>"); //结尾标志

    //词典进行匹配
    public static Map<String, Set<String>> dicMatch(String line){
        Map<String, Set<String>> res_dic= new HashMap<String, Set<String>>();
        int lineLen = line.length();
        int index = 0;
        while(index < lineLen){
            int end  = lineLen <= index + maxWordLen? lineLen: index + maxWordLen;
            String tmp_s = line.substring(index, end);
            boolean find = false;
            for(int i = tmp_s.length(); i >= 0; i--){
                String tw = tmp_s.substring(0,i);
                Set<String> iscontain = isTreeContain(tw);
                if(iscontain != null && iscontain.size() > 0){
                    index = index + i;
                    res_dic.put(tw, iscontain);
                    find = true;
                    break;
                }
            }
            if(!find){
                index = index + 1;
            }
        }
        return res_dic;
    }

    //是否包含词典
    private static Set<String> isTreeContain(String word){
        int wordlen = word.length();
        Set<String> res = null;
        TreeNode curr = head;
        int i= 0;
        for(i = 0; i < wordlen; i++){
            if(curr.getChild() == null){
                res = null;
                break;
            }else{
                List<TreeNode> child = curr.getChild();
                TreeNode tmptree = new TreeNode(word.charAt(i) + "");
                if(!child.contains(tmptree)){
                    res = null;
                    break;
                }else{
                    curr = child.get(child.indexOf(tmptree));
                }
            }
        }
        if(!curr.getChild().contains(endNode) || i < wordlen){
            res = null;
        }else if(i == wordlen && curr.getChild().contains(endNode)){
            return curr.getChild().get(curr.getChild().indexOf(endNode)).getLableList();
        }
        return res;
    }


    //词典构建和初始化
    public static void initSearchParm(String filePath) throws Exception{
        String fileContent = readAllFile(filePath);
        String[] words = fileContent.split("\n");
        System.out.println("file line count :" + words.length);
        long t1 = System.currentTimeMillis();
        buildTree(words);
        System.out.println("build dic time : " + (System.currentTimeMillis() - t1));
    }

    static String readAllFile(String filename) throws Exception {
        File file = new File(filename);
        Long len = file.length();
        byte[] filecontent = new byte[len.intValue()];
        FileInputStream in = new FileInputStream(file);
        in.read(filecontent);
        in.close();
        String content = new String(filecontent, "utf-8");
        return content;
    }

    static void buildTree(String[] words){
        for(String s : words){
            s = s.trim();
            String lable = s.split("\t")[1];
            String name = s.split("\t")[0];

            List<String> token = getOneWordList(name);
            TreeNode curr = head;
            for(String w : token){
                TreeNode node = new TreeNode(w);
                if(curr.getChild() !=null){
                    if(curr.getChild().contains(node)){
                        List<TreeNode> child = curr.getChild();
                        curr = child.get(child.indexOf(node));
                        if(node.equals(endNode)){ //新增标签
                            Set<String> lableSet = curr.getLableList();
                            lableSet.add(lable);
                        }
                    }else{
                        List<TreeNode> child = curr.getChild();
                        child.add(node);
                        curr = child.get(child.indexOf(node));
                        //添加多标签
                        if(node.equals(endNode)){ //新增标签
                            Set<String> lableSet = curr.getLableList();
                            if(lableSet == null){
                                lableSet = new HashSet<String>();
                                lableSet.add(lable);
                                node.setLableList(lableSet);
                            }else {
                                lableSet.add(lable);
                            }
                        }
                    }
                }else{
                    List<TreeNode> child = new ArrayList<TreeNode>();
                    child.add(node);
                    if(node.equals(endNode)){ //新增标签
                        Set<String> lableSet = new HashSet<String>();
                        lableSet.add(lable);
                        node.setLableList(lableSet);
                    }
                    curr.setChild(child);
                    curr = child.get(child.indexOf(node));
                }
            }
        }
    }

    static List<String> getOneWordList(String line){
        List<String> res = new ArrayList<String>();
        allWord.add(line);
        int wordlen = line.trim().length();
        updataMaxLen(wordlen);
        for(int j = 0; j < wordlen; j++) {
            String w = line.charAt(j) + "";
            res.add(w);
        }
        res.add("<eos>");
        return res;
    }

    static void updataMaxLen(int len){
        if(len > maxWordLen){
            maxWordLen = len;
        }
    }

    static int getMaxWordLen(){
        return maxWordLen;
    }




