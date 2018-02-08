# mas-data-process-
火星电离层MGS数据处理
mgs定义了getListFiles(path)函数获得当前路径文件夹所有的eds文件路径。
定义getline(thefilepath, desired_line_number)读取文本文档的数据，thefilepath为文件夹路径，desired_line_number为要读取的起始路径，读取数据为从指定
行到最后一行的全部数据，返回读取数据矩阵。
