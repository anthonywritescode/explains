#include <sass/context.h>
#include <stdio.h>


int main(void) {
    const char* src = "a { color: red; width: 2 * 2px; }";
    struct Sass_Data_Context *data_ctx = sass_make_data_context(
        sass_copy_c_string(src)
    );

    sass_compile_data_context(data_ctx);

    struct Sass_Context *ctx = sass_data_context_get_context(data_ctx);
    const char* output = sass_context_get_output_string(ctx);

    printf("output: %s\n", output);

    return 0;
}
