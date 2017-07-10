# compute shader
# version 430

layout ( local_size_x = 1000 ) in;

layout(std430, binding=0) buffer SSB1 {
	float[111][66] layout;
};

layout(std430, binding=0) buffer SSB1 {
	float[66][3] layout;
};

void main() {
	...
}