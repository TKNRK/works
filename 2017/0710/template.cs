# compute shader
# version 430

layout ( local_size_x = 1000 ) in;

layout(std430, binding=0) buffer SSB1 {
	float[NUM_OF_NODES][DIMENTION] layout;
};

layout(std430, binding=0) buffer SSB1 {
	float[DIMENTION][3] layout;
};

void main() {
	...
}