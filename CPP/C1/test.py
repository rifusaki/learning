from statistics import mean

sumtot = 0
countot = 0
print('Sum, count and average calculator!')

lst = [34, 197, 8, 127, 25, 247, 298, 243, 6, 108, 264, 245, 276, 172, 174, 278, 222, 24, 275, 53, 200, 43, 177, 128, 127, 59, 143, 48, 177, 91, 263, 63, 36, 189, 23, 176, 280, 233, 102, 275, 30, 40, 246, 124, 210, 282, 220, 203, 275, 138, 273, 154, 196, 41, 233, 234, 177, 164, 137, 3, 113, 71, 290, 160, 243, 31, 78, 236, 102, 152, 105, 106, 218, 129, 285, 137, 293, 243, 183, 228, 91, 45, 230, 300, 214, 285, 267, 233, 85, 75, 241, 246, 262, 226, 134, 71, 77, 70, 152, 64, 286, 147, 212, 248, 25, 24, 32, 77, 116, 113, 294, 29, 220, 225, 111, 190, 120, 162, 188, 299, 163, 78, 58, 177, 85, 158, 90, 127, 217, 58, 55, 270, 137, 299, 296, 188, 114, 63, 48, 127, 141, 296, 281, 160, 179, 132, 269, 129, 119, 139, 271, 168, 162, 222, 13, 162, 233, 164, 142, 258, 280, 201, 239, 87, 128, 16, 106, 41, 225, 171, 261, 217, 275, 140, 96, 297, 275, 220, 300, 26, 62, 132, 136, 258, 102, 39, 3, 42, 200, 204, 241, 231, 216, 206, 67, 204, 264, 217, 44, 110, 249, 31, 61, 78, 145, 34, 68, 268, 213, 84, 66, 260, 36, 219, 180, 244, 299, 179, 36, 197, 49, 146, 3, 297, 49, 216, 256, 67, 266, 251, 226, 177, 221, 170, 204, 267, 5, 99, 141, 125, 16, 249, 220, 188, 157, 116, 195, 59, 214, 262, 59, 71, 277, 109, 222, 227, 163, 37, 211, 247, 210, 247, 240, 94, 275, 62, 185, 29, 115, 48, 49, 43, 274, 108, 52, 108, 82, 27, 30, 24, 285, 93, 114, 253, 166, 111, 76, 203, 183, 122, 204, 251, 221, 26, 53, 171, 31, 35, 64, 101, 26, 216, 142, 214, 275, 263, 259, 152, 288, 145, 68, 253, 219, 185, 265, 203, 254, 203, 18, 125, 35, 68, 54, 211, 49, 247, 174, 174, 75, 132, 21, 167, 264, 47, 284, 294, 85, 142, 30, 180, 297, 63, 6, 82, 127, 168, 47, 211, 122, 194, 262, 28, 62, 170, 70, 184, 136, 294, 107, 158, 291, 209, 86, 42, 174, 276, 141, 235, 190, 179, 48, 159, 17, 176, 22, 108, 208, 8, 180, 152, 57, 209, 100, 230, 243, 76, 265, 165, 241, 287, 92, 127, 203, 22, 91, 249, 190, 81, 88, 210, 131, 88, 70, 146, 295, 49, 267, 249, 280, 272, 69, 290, 85, 89, 249, 6, 187, 256, 189, 73, 117, 276, 147, 194, 16, 241, 207, 286, 227, 206, 204, 282, 148, 45, 253, 249, 1, 190, 4, 118, 42, 195, 148, 299, 144, 69, 165, 239, 9, 54, 105, 232, 210, 192, 63, 113, 9, 68, 56, 281, 99, 238, 69, 31, 234, 8, 252, 78, 144, 221, 211, 162, 56, 278, 154, 160, 139, 211, 229, 110, 89, 116, 64, 40, 23, 156, 88, 168, 275, 199, 240, 213, 126, 145, 138, 113, 168, 279, 167, 220, 233, 241, 40, 16, 272, 30, 275, 11, 20, 298, 191, 91, 161, 285, 222, 245, 229, 146, 287, 85, 38, 132, 78, 121, 249, 82, 194, 8, 235, 196, 109, 142, 268, 179, 254, 250, 44, 70, 200, 120, 289, 200, 168, 268, 60, 179, 219, 128, 180, 134, 197, 16, 53, 215, 6, 236, 110, 156, 21, 58, 190, 134, 210, 5, 70, 195, 126, 206, 99, 69, 230, 142, 258, 179, 109, 231, 151, 138, 13, 37, 219, 231, 223, 19, 217, 34, 159, 144, 93, 163, 178, 236, 84, 141, 161, 39, 53, 100, 233, 170, 37, 63, 107, 274, 225, 192, 121, 25, 4, 167, 225, 222, 69, 15, 93, 152, 220, 9, 299, 291, 222, 268, 300, 35, 114, 23, 257, 185, 261, 139, 33, 203, 107, 46, 106, 225, 94, 249, 18, 261, 33, 241, 119, 207, 75, 201, 133, 198, 266, 205, 104, 226, 5, 127, 268, 41, 214, 79, 128, 262, 237, 192, 51, 68, 30, 148, 278, 293, 207, 247, 55, 264, 184, 44, 250, 62, 25, 288, 173, 103, 111, 266, 164, 66, 190, 146, 254, 105, 144, 49, 236, 297, 184, 137, 48, 110, 286, 268, 76, 165, 218, 30, 177, 87, 256, 211, 264, 260, 227, 168, 251, 175, 267, 52, 147, 254, 143, 86, 28, 209, 288, 241, 66, 253, 118, 196, 283, 240, 230, 287, 38, 42, 243, 271, 37, 180, 106, 119, 20, 56, 99, 45, 166, 202, 278, 70, 146, 12, 203, 254, 92, 65, 77, 142, 199, 227, 68, 11, 279, 208, 121, 3, 115, 192, 74, 188, 236, 12, 2, 288, 10, 39, 201, 297, 29, 178, 23, 244, 118, 233, 153, 260, 175, 115, 112, 219, 164, 62, 170, 145, 32, 156, 239, 215, 80, 72, 98, 133, 90, 13, 230, 78, 67, 55, 131, 163, 155, 205, 179, 21, 271, 218, 286, 218, 159, 103, 2, 93, 282, 22, 94, 149, 283, 10, 71, 285, 211, 212, 92, 172, 216, 152, 188, 70, 175, 270, 68, 297, 81, 247, 61, 118, 218, 100, 300, 119, 273, 206, 287, 268, 139, 181, 30, 275, 187, 168, 130, 294, 90, 280, 267, 285, 35, 8, 85, 36, 200, 22, 46, 45, 169, 203, 116, 96, 265, 92, 3, 144, 182, 206, 132, 94, 45, 224, 204, 117, 104, 203, 162, 102, 124, 224, 286, 207, 11, 177, 132, 222, 215, 121, 170, 15, 244, 219, 131, 151, 115, 290, 138, 262, 165, 108, 283, 200, 27, 191, 9, 169, 49, 50, 290, 74, 69, 184, 276, 271, 283, 259, 148, 167, 90, 32, 300, 78, 156, 92, 171, 282, 106, 292, 59, 143, 69, 260, 274, 256, 126, 81, 116, 68, 64, 242, 71, 282, 203, 41, 110, 38, 149, 136, 203, 226, 130, 119, 295, 32, 72, 157, 112, 209, 137, 170, 34, 228, 177, 259, 215, 36, 65, 73, 220, 264, 36, 296, 204, 46, 136, 19, 156, 290, 138, 11, 55, 57, 52, 135, 186, 51, 258, 126, 143, 60, 192, 162, 245, 178, 50, 98, 178, 62, 240, 35, 147, 251, 137, 252, 85, 257, 247, 68, 205, 143, 189, 69, 23, 190, 73, 151, 140, 142, 298, 127, 65, 221, 117, 127, 50, 122, 192, 102, 80, 28, 202, 257, 148, 113, 300, 42, 191, 126, 160, 103, 226, 226, 295, 69, 51, 87, 206, 20, 131, 99, 119, 209, 18, 12, 47, 233, 83, 250, 190, 52, 182, 218, 40, 49, 153, 28, 158, 259, 163, 63, 51, 125, 287, 45, 93, 83, 46, 149, 151, 178, 205, 1, 229, 269, 51, 165, 112, 181, 100, 231, 145, 67, 158, 57, 16, 110, 209, 278, 263, 204, 81, 159, 55, 279, 27, 244, 193, 130, 228, 51, 118, 153, 173, 145, 172, 80, 151, 181, 150, 145, 120, 297, 233, 158, 53, 111, 32, 54, 118, 28, 291, 173, 19, 215, 217, 259, 280, 76, 188, 198, 283, 34, 2, 67, 282, 134, 288, 139, 239, 209, 120, 146, 110, 182, 44, 63, 69, 254, 250, 20, 254, 47, 56, 15, 177, 210, 50, 210, 140, 278, 41, 277, 222, 4, 287, 178, 253, 123, 146, 81, 36, 252, 291, 230, 274, 177, 44, 136, 59, 149, 100, 45, 208, 147, 45, 170, 185, 238, 240, 223, 246, 207, 17, 1, 262, 263, 55, 68, 264, 86, 276, 155, 128, 195, 3, 212, 161, 84, 156, 229, 211, 197, 165, 86, 262, 285, 28, 60, 230, 75, 219, 297, 114, 139, 116, 93, 23, 148, 91, 127, 125, 294, 238, 279, 73, 137, 115, 93, 223, 268, 173, 273, 231, 96, 35, 80, 55, 115, 161, 235, 298, 184, 297, 157, 117, 129, 139, 232, 167, 102, 49, 292, 94, 151, 19, 207, 195, 251, 18, 85, 291, 214, 188, 209, 293, 292, 294, 248, 61, 152, 192, 260, 166, 73, 220, 120, 95, 196, 74, 107, 221, 202, 298, 249, 250, 95, 174, 10, 128, 5, 196, 197, 288, 25, 140, 12, 82, 163, 244, 183, 97, 263, 111, 227, 53, 108, 17, 271, 112, 279, 281, 153, 36, 80, 54, 169, 15, 286, 81, 289, 294, 21, 92, 214, 296, 145, 201, 242, 258, 58, 198, 131, 168, 41, 258, 294, 125, 45, 47, 156, 103, 177, 97, 300, 163, 170, 70, 182, 128, 282, 186, 154, 164, 152, 243, 286, 206, 200, 232, 163, 136, 283, 9, 106, 16, 273, 12, 110, 105, 165, 295, 208, 127, 157, 51, 276, 229, 245, 91, 271, 125, 232, 236, 142, 127, 168, 189, 8, 97, 251, 139, 123, 235, 104, 220, 167, 93, 262, 224, 203, 85, 261, 242, 264, 121, 115, 70, 13, 20, 111, 188, 258, 107, 28, 235, 126, 100, 20, 105, 78, 193, 189, 248, 141, 187, 280, 188, 243, 63, 243, 195, 6, 264, 73, 221, 132, 294, 226, 127, 287, 47, 144, 110, 91, 293, 219, 250, 188, 50, 288, 204, 181, 145, 192, 146, 57, 133, 106, 204, 152, 153, 285, 155, 29, 222, 174, 66, 278, 271, 74, 153, 109, 265, 296, 74, 232, 42, 260, 16, 148, 170, 15, 142, 93, 23, 96, 61, 135, 292, 192, 224, 14, 202, 30, 267, 145, 93, 239, 185, 262, 100, 299, 266, 214, 10, 268, 62, 274, 236, 204, 184, 153, 238, 247, 217, 128, 118, 73, 257, 122, 233, 38, 55, 71, 200, 78, 163, 172, 175, 223, 205, 52, 268, 125, 236, 254, 106, 284, 25, 162, 89, 163, 184, 198, 254, 221, 264, 202, 40, 268, 120, 192, 278, 153, 66, 225, 154, 6, 1, 63, 43, 137, 122, 26, 227, 212, 45, 260, 93, 15, 227, 29, 6, 68, 3, 156, 31, 57, 115, 78, 124, 33, 237, 54, 16, 74, 19, 223, 190, 28, 274, 63, 236, 66, 290, 268, 147, 19, 138, 50, 94, 73, 111, 275, 47, 285, 139, 162, 257, 296, 36, 36, 29, 253, 71, 298, 181, 171, 164, 283, 167, 277, 124, 132, 239, 159, 165, 97, 165, 152, 249, 261, 199, 83, 170, 110, 101, 73, 299, 283, 219, 201, 276, 262, 26, 101, 281, 105, 254, 288, 249, 102, 45, 90, 228, 123, 288, 265, 99, 217, 98, 160, 237, 42, 283, 8, 223, 228, 179, 298, 95, 76, 58, 29, 195, 109, 205, 186, 39, 129, 37, 273, 64, 63, 203, 159, 89, 30, 298, 101, 29, 119, 1, 170, 23, 185, 129, 91, 147, 234, 74, 59, 189, 252, 246, 124, 214, 159, 203, 13, 176, 191, 62, 286, 79, 6, 57, 145, 18, 96, 162, 42, 45, 96, 190, 270, 275, 281, 283, 264, 152, 147, 34, 231, 22, 186, 210, 95, 254, 265, 11, 232, 8, 179, 10, 172, 271, 171, 244, 219, 273, 174, 65, 177, 102, 70, 19, 235, 258, 271, 222, 273, 51, 20, 204, 181, 143, 110, 193, 211, 165, 2, 282, 156, 157, 121, 31, 94, 216, 115, 190, 223, 226, 45, 73, 234, 53, 25, 201, 131, 275, 294, 246, 71, 201, 258, 103, 204, 123, 278, 5, 141, 163, 170, 113, 149, 3, 269, 35, 130, 59, 125, 232, 90, 24, 291, 290, 201, 133, 84, 261, 157, 38, 98, 158, 45, 46, 80, 249, 293, 284, 259, 107, 291, 234, 168, 26, 9, 229, 212, 192, 103, 239, 69, 278, 111, 240, 291, 228, 241, 46, 203, 132, 27, 44, 94, 80, 219, 187, 264, 130, 251, 220, 274, 143, 277, 125, 234, 231, 221, 82, 50, 17, 204, 26, 37, 250, 63, 230, 277, 47, 247, 133, 183, 279, 186, 174, 8, 171, 263, 6, 13, 231, 280, 220, 97, 254, 149, 180, 205, 11, 109, 91, 36, 114, 260, 208, 1, 22, 231, 264, 209, 271, 94, 290, 92, 163, 184, 63, 130, 198, 148, 252, 45, 93, 97, 167, 103, 144, 283, 6, 139, 143, 215, 132, 36, 111, 64, 150, 177, 174, 218, 279, 118, 233, 204, 13, 244, 220, 104, 46, 31, 116, 71, 184, 120, 132, 60, 190, 284, 225, 260, 280, 5, 84, 72, 206, 257]

print("avg:", mean(lst), "\ncount:", len(lst), "\nsum:", sum(lst), "\n\n")

for num in range(10, 16):
   for i in range(2, num):
       if num%i == 0:
          print(num)
          break
       
print("\n")
sum=0
for i in range(1, 50000):
   if i%3==0 or i%7==0:
      sum+=i
print("\n",sum)