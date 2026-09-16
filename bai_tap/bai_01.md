## Báo cáo: Sự Rẽ Nhánh OpenOffice - LibreOffice và Các Bài Học từ Mâu Thuẫn Cộng Đồng

### Giới thiệu

Một trong những trường hợp điển hình của sự rẽ nhánh (fork) do mâu thuẫn cộng đồng trong phần mềm mã nguồn mở là **LibreOffice** tách biệt từ **OpenOffice.org**. Sự kiện này xảy ra vào năm 2010 và là kết quả của những xung đột trong quản trị dự án cũng như những khác biệt về tầm nhìn phát triển.

### Nguyên nhân của Sự Rẽ Nhánh

**Sự thay đổi chiến lược của Oracle**: Sau khi mua Sun Microsystems vào năm 2009, Oracle đã thay đổi chiến lược phát triển OpenOffice. Thay vì tiếp tục hỗ trợ mã nguồn mở hoàn toàn, Oracle tập trung vào các bản phát hành ít thường xuyên hơn và kiểm soát chặt chẽ hơn các tính năng phát triển.

**Khác biệt về tầm nhìn**: Cộng đồng OpenOffice.org muốn một dự án hoàn toàn mã nguồn mở, với quyết định được đưa ra dân chủ. Tuy nhiên, Oracle muốn duy trì sự kiểm soát chiến lược và hướng phát triển của dự án.

**Thiếu minh bạch**: Oracle không công bố rõ ràng kế hoạch dài hạn cho OpenOffice, khiến cộng đồng lập trình viên cảm thấy bất an về tương lai dự án.

### Sự Khởi Động LibreOffice

Vào năm 2010, một nhóm các nhà phát triển hàng đầu của OpenOffice đã rẽ nhánh dự án và tạo ra **LibreOffice** dưới sự quản lý của **The Document Foundation**, một tổ chức độc lập phi lợi nhuận.

LibreOffice được xây dựng trên cơ sở mã OpenOffice nhưng với:
- Quyết định được đưa ra bởi cộng đồng
- Các bản cập nhật thường xuyên và tính năng mới
- Hợp tác mở rộng với các nhà phát triển toàn cầu

### Hậu Quả của Sự Rẽ Nhánh

**Sự suy thoái của OpenOffice**: OpenOffice dần mất đi sự ủng hộ của cộng đồng và các công ty. Năm 2011, Oracle trao OpenOffice cho Apache Software Foundation, nhưng dự án này vẫn không phục hồi được lực hút từ trước đó.

**Thành công của LibreOffice**: Ngược lại, LibreOffice phát triển mạnh mẽ với các bản phát hành thường xuyên, tích hợp c��c tính năng hiện đại, và nhận được sự ủng hộ từ các chính phủ và tổ chức giáo dục trên toàn thế giới.

**Bài học về Quản trị Dự án**: Sự rẽ nhánh này cho thấy tầm quan trọng của việc duy trì sự tin tưởng và minh bạch trong cộng đồng mã nguồn mở. Khi các nhà lãnh đạo dự án không lắng nghe cộng đồng hoặc làm suy yếu giá trị mã nguồn mở, họ có nguy cơ mất đi các thành viên cộng đồng quan trọng.

### Kết luận

Trường hợp OpenOffice - LibreOffice minh họa rằng sự thất bại của một dự án mã nguồn mở không luôn do yếu tố kỹ thuật, mà có thể do các quyết định quản trị và thiếu sự giao tiếp với cộng đồng. Sự thành công lâu dài của các dự án mã nguồn mở phụ thuộc vào việc duy trì sự tin tưởng, minh bạch, và tôn trọng giá trị cộng đồng.

---

## Bài 1.3: Tragedy of the Commons trong Phần Mềm Mã Nguồn Mở

### Khái Niệm Tragedy of the Commons

Tragedy of the Commons (Bi kịch của những tài sản chung) là một khái niệm kinh tế xã hội mô tả tình huống trong đó các cá nhân hoặc tổ chức, hành động dựa trên lợi ích riêng của mình, cuối cùng dẫn đến kết quả tiêu cực cho toàn bộ cộng đồng. Trong ngữ cảnh phần mềm mã nguồn mở, tài sản chung chính là các thư viện hạ tầng được nhiều tổ chức sử dụng nhưng không ai có trách nhiệm chính thức bảo trì và cập nhật.

### Trường Hợp OpenSSL (Trước Năm 2014)

OpenSSL là một thư viện mã nguồn mở cung cấp các công cụ mã hóa SSL/TLS được sử dụng rộng rãi trên internet. Trước năm 2014, OpenSSL là một ví dụ điển hình về tragedy of the commons. Hàng tỷ thiết bị và ứng dụng toàn cầu phụ thuộc vào OpenSSL để bảo mật kết nối internet. Tuy nhiên, dự án này được duy trì bởi một nhóm nhỏ các tình nguyện viên với nguồn lực cực kỳ hạn chế.

Tình huống trở nên nghiêm trọng vào tháng 4 năm 2014 khi lỗ hổng Heartbleed được công bố. Đây là một lỗ hổng bảo mật nghiêm trọng cho phép kẻ tấn công đọc bộ nhớ từ các máy chủ đang sử dụng OpenSSL, khiến rò rỉ khóa mã hóa, mật khẩu và thông tin nhạy cảm khác. Lỗ hổng này tồn tại trong mã OpenSSL trong hai năm mà không được phát hiện, phần lớn vì sự thiếu kiểm tra mã kỹ lưỡng.

Nguyên nhân gốc rễ của vấn đề này là: các tổ chức lớn (như Google, Microsoft, Facebook) và hàng triệu công ty nhỏ đều sử dụng OpenSSL nhưng hầu như không ai đầu tư nguồn lực để phát triển hay bảo trì nó. Mỗi tổ chức đều hưởng lợi từ phần mềm miễn phí, nhưng không ai cảm thấy có trách nhiệm hoặc động lực cấp nguồn lực đó. Đây chính là tragedy of the commons: tất cả mọi người hưởng lợi từ tài sản chung, nhưng tất cả mọi người cũng để cho nó suy thoái.

### Cơ Chế Khắc Phục Đề Xuất

Để giải quyết tragedy of the commons trong phần mềm mã nguồn mở, cần áp dụng các cơ chế sau:

**1. Mô Hình Tài Trợ Tập Thể**: Thành lập các quỹ hoặc hiệp hội nơi các tổ chức sử dụng phần mềm đóng góp theo tỷ lệ lợi ích họ nhận được. Ví dụ, Linux Foundation đã thành công với mô hình này, nơi các công ty lớn công khai cam kết tài trợ cho các dự án quan trọng như Linux kernel.

**2. Yêu Cầu Mã Nguồn Mở**: Các chính phủ và tổ chức lớn có thể yêu cầu các nhà cung cấp phần mềm công khai tài trợ cho các thư viện mã nguồn mở mà họ phụ thuộc vào. Điều này tạo động lực kinh tế trực tiếp.

**3. Công Khai Hóa Gánh Nặng Bảo Trì**: Công khai rõ ràng chi phí bảo trì thực tế và số lượng lỏng lẻo trong nhân lực. Khi các tổ chức nhận thức được chi phí tiềm ẩn, họ sẽ có động lực đầu tư.

**4. Huy Động Tình Nguyện Chuyên Nghiệp**: Thay vì dựa hoàn toàn vào tình nguyện viên, các dự án nên có các nhân viên được trả lương chính thức để bảo trì code. OpenSSL Foundation sau Heartbleed đã áp dụng chiến lược này thành công.

**5. Kiểm Toán Bảo Mật Bắt Buộc**: Các thư viện hạ tầng quan trọng nên được kiểm toán bảo mật thường xuyên bởi các bên thứ ba, với chi phí do các tổ chức sử dụng chịu trách nhiệm.

### Kết Luận

Sự cố Heartbleed của OpenSSL là một bài học quí báu cho cộng đồng mã nguồn mở. Nó chứng minh rằng tragedy of the commons có thể có hậu quả thảm khốc khi áp dụng cho các thành phần hạ tầng quan trọng. Bằng cách áp dụng các cơ chế tài trợ tập thể, công khai hóa chi phí, và chuyên nghiệp hóa bảo trì, cộng đồng mã nguồn mở có thể ngăn chặn những bi kịch tương tự trong tương lai.
