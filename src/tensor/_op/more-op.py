is_tensor

Returns True if obj is a PyTorch tensor.

is_storage

Returns True if obj is a PyTorch storage object.

is_complex

Returns True if the data type of input is a complex data type i.e., one of torch.complex64, and torch.complex128.

is_floating_point

Returns True if the data type of input is a floating point data type i.e., one of torch.float64, torch.float32, torch.float16, and torch.bfloat16.

is_nonzero

Returns True if the input is a single element tensor which is not equal to zero after type conversions.

set_default_dtype

Sets the default floating point dtype to d.

get_default_dtype

Get the current default floating point torch.dtype.

set_default_tensor_type

Sets the default torch.Tensor type to floating point tensor type t.

numel

Returns the total number of elements in the input tensor.

set_printoptions

Set options for printing.

set_flush_denormal

Disables denormal floating numbers on CPU.

Creation Ops
NOTE

Random sampling creation ops are listed under Random sampling and include: torch.rand() torch.rand_like() torch.randn() torch.randn_like() torch.randint() torch.randint_like() torch.randperm() You may also use torch.empty() with the In-place random sampling methods to create torch.Tensor s with values sampled from a broader range of distributions.

tensor

Constructs a tensor with data.

sparse_coo_tensor

Constructs a sparse tensor in COO(rdinate) format with specified values at the given indices.

as_tensor

Convert the data into a torch.Tensor.

as_strided

Create a view of an existing torch.Tensor input with specified size, stride and storage_offset.

from_numpy

Creates a Tensor from a numpy.ndarray.

zeros

Returns a tensor filled with the scalar value 0, with the shape defined by the variable argument size.

zeros_like

Returns a tensor filled with the scalar value 0, with the same size as input.

ones

Returns a tensor filled with the scalar value 1, with the shape defined by the variable argument size.

ones_like

Returns a tensor filled with the scalar value 1, with the same size as input.

arange

Returns a 1-D tensor of size \left\lceil \frac{\text{end} - \text{start}}{\text{step}} \right\rceil⌈ 
step
end−start
​	
 ⌉ with values from the interval [start, end) taken with common difference step beginning from start.

range

Returns a 1-D tensor of size \left\lfloor \frac{\text{end} - \text{start}}{\text{step}} \right\rfloor + 1⌊ 
step
end−start
​	
 ⌋+1 with values from start to end with step step.

linspace

Creates a one-dimensional tensor of size steps whose values are evenly spaced from start to end, inclusive.

logspace

Creates a one-dimensional tensor of size steps whose values are evenly spaced from {{\text{{base}}}}^{{\text{{start}}}}base 
start
  to {{\text{{base}}}}^{{\text{{end}}}}base 
end
 , inclusive, on a logarithmic scale with base base.

eye

Returns a 2-D tensor with ones on the diagonal and zeros elsewhere.

empty

Returns a tensor filled with uninitialized data.

empty_like

Returns an uninitialized tensor with the same size as input.

empty_strided

Returns a tensor filled with uninitialized data.

full

Creates a tensor of size size filled with fill_value.

full_like

Returns a tensor with the same size as input filled with fill_value.

quantize_per_tensor

Converts a float tensor to a quantized tensor with given scale and zero point.

quantize_per_channel

Converts a float tensor to a per-channel quantized tensor with given scales and zero points.

dequantize

Returns an fp32 Tensor by dequantizing a quantized Tensor

complex

Constructs a complex tensor with its real part equal to real and its imaginary part equal to imag.

polar

Constructs a complex tensor whose elements are Cartesian coordinates corresponding to the polar coordinates with absolute value abs and angle angle.

heaviside

Computes the Heaviside step function for each element in input.

Indexing, Slicing, Joining, Mutating Ops
cat

Concatenates the given sequence of seq tensors in the given dimension.

chunk

Splits a tensor into a specific number of chunks.

dsplit

Splits input, a tensor with three or more dimensions, into multiple tensors depthwise according to indices_or_sections.

column_stack

Creates a new tensor by horizontally stacking the tensors in tensors.

dstack

Stack tensors in sequence depthwise (along third axis).

gather

Gathers values along an axis specified by dim.

hsplit

Splits input, a tensor with one or more dimensions, into multiple tensors horizontally according to indices_or_sections.

hstack

Stack tensors in sequence horizontally (column wise).

index_select

Returns a new tensor which indexes the input tensor along dimension dim using the entries in index which is a LongTensor.

masked_select

Returns a new 1-D tensor which indexes the input tensor according to the boolean mask mask which is a BoolTensor.

movedim

Moves the dimension(s) of input at the position(s) in source to the position(s) in destination.

moveaxis

Alias for torch.movedim().

narrow

Returns a new tensor that is a narrowed version of input tensor.

nonzero

reshape

Returns a tensor with the same data and number of elements as input, but with the specified shape.

row_stack

Alias of torch.vstack().

scatter

Out-of-place version of torch.Tensor.scatter_()

scatter_add

Out-of-place version of torch.Tensor.scatter_add_()

split

Splits the tensor into chunks.

squeeze

Returns a tensor with all the dimensions of input of size 1 removed.

stack

Concatenates a sequence of tensors along a new dimension.

swapaxes

Alias for torch.transpose().

swapdims

Alias for torch.transpose().

t

Expects input to be <= 2-D tensor and transposes dimensions 0 and 1.

take

Returns a new tensor with the elements of input at the given indices.

take_along_dim

Selects values from input at the 1-dimensional indices from indices along the given dim.

tensor_split

Splits a tensor into multiple sub-tensors, all of which are views of input, along dimension dim according to the indices or number of sections specified by indices_or_sections.

tile

Constructs a tensor by repeating the elements of input.

transpose

Returns a tensor that is a transposed version of input.

unbind

Removes a tensor dimension.

unsqueeze

Returns a new tensor with a dimension of size one inserted at the specified position.

vsplit

Splits input, a tensor with two or more dimensions, into multiple tensors vertically according to indices_or_sections.

vstack

Stack tensors in sequence vertically (row wise).

where

Return a tensor of elements selected from either x or y, depending on condition.

Generators
Generator

Creates and returns a generator object that manages the state of the algorithm which produces pseudo random numbers.

Random sampling
seed

Sets the seed for generating random numbers to a non-deterministic random number.

manual_seed

Sets the seed for generating random numbers.

initial_seed

Returns the initial seed for generating random numbers as a Python long.

get_rng_state

Returns the random number generator state as a torch.ByteTensor.

set_rng_state

Sets the random number generator state.

torch.default_generator Returns the default CPU torch.Generator
bernoulli

Draws binary random numbers (0 or 1) from a Bernoulli distribution.

multinomial

Returns a tensor where each row contains num_samples indices sampled from the multinomial probability distribution located in the corresponding row of tensor input.

normal

Returns a tensor of random numbers drawn from separate normal distributions whose mean and standard deviation are given.

poisson

Returns a tensor of the same size as input with each element sampled from a Poisson distribution with rate parameter given by the corresponding element in input i.e.,

rand

Returns a tensor filled with random numbers from a uniform distribution on the interval [0, 1)[0,1)

rand_like

Returns a tensor with the same size as input that is filled with random numbers from a uniform distribution on the interval [0, 1)[0,1).

randint

Returns a tensor filled with random integers generated uniformly between low (inclusive) and high (exclusive).

randint_like

Returns a tensor with the same shape as Tensor input filled with random integers generated uniformly between low (inclusive) and high (exclusive).

randn

Returns a tensor filled with random numbers from a normal distribution with mean 0 and variance 1 (also called the standard normal distribution).

randn_like

Returns a tensor with the same size as input that is filled with random numbers from a normal distribution with mean 0 and variance 1.

randperm

Returns a random permutation of integers from 0 to n - 1.

In
In-place random sampling
There are a few more in-place random sampling functions defined on Tensors as well. Click through to refer to their documentation:

torch.Tensor.bernoulli_() - in-place version of torch.bernoulli()

torch.Tensor.cauchy_() - numbers drawn from the Cauchy distribution

torch.Tensor.exponential_() - numbers drawn from the exponential distribution

torch.Tensor.geometric_() - elements drawn from the geometric distribution

torch.Tensor.log_normal_() - samples from the log-normal distribution

torch.Tensor.normal_() - in-place version of torch.normal()

torch.Tensor.random_() - numbers sampled from the discrete uniform distribution

torch.Tensor.uniform_() - numbers sampled from the continuous uniform distribution

Quasi-random sampling
quasirandom.SobolEngine

The torch.quasirandom.SobolEngine is an engine for generating (scrambled) Sobol sequences.

Serialization
save

Saves an object to a disk file.

load

Loads an object saved with torch.save() from a file.

Parallelism
get_num_threads

Returns the number of threads used for parallelizing CPU operations

set_num_threads

Sets the number of threads used for intraop parallelism on CPU.

get_num_interop_threads

Returns the number of threads used for inter-op parallelism on CPU (e.g.

set_num_interop_threads

Sets the number of threads used for interop parallelism (e.g.

Locally disabling gradient computation
The context managers torch.no_grad(), torch.enable_grad(), and torch.set_grad_enabled() are helpful for locally disabling and enabling gradient computation. See Locally disabling gradient computation for more details on their usage. These context managers are thread local, so they won’t work if you send work to another thread using the threading module, etc.

Examples:

>>> x = torch.zeros(1, requires_grad=True)
>>> with torch.no_grad():
...     y = x * 2
>>> y.requires_grad
False

>>> is_train = False
>>> with torch.set_grad_enabled(is_train):
...     y = x * 2
>>> y.requires_grad
False

>>> torch.set_grad_enabled(True)  # this can also be used as a function
>>> y = x * 2
>>> y.requires_grad
True

>>> torch.set_grad_enabled(False)
>>> y = x * 2
>>> y.requires_grad
False
no_grad

Context-manager that disabled gradient calculation.

enable_grad

Context-manager that enables gradient calculation.

set_grad_enabled

Context-manager that sets gradient calculation to on or off.

