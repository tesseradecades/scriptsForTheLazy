#IMPLEMENTING THE CAESAR CIPHER
def codeMessage(c, rot, message)
	newMessage = Array.new
	message.split.each do |a|
		word = ''
		a.split('').each do |x|
			eString = ''
			if c == "decode"
				word += decode(rot, x)
			elsif c == "encode"
				word += encode(rot, x)
			end
		end
		newMessage << word
	end
	return newMessage.join(" ")
end

def decode(rot, ch)
	o = ch.downcase.ord-rot.to_i
	if (o < 97)
		o+=26
	elsif (o > 122)
		o-=26
	end
	return o.chr.to_s.upcase
end

def encode(rot, ch)
	o = ch.downcase.ord+rot.to_i
	if (o < 97)
		o+=26
	elsif (o > 122)
		o-=26
	end
	return o.chr.to_s.upcase
end

#CRACKING THE CAESAR CIPHER w/ least square
def crack(message)
	realFreq = Array[8.1, 1.5, 2.8, 4.3, 13.0, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 7.0, 2.4,6.8, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]
	#Step 1 Calculate letter frequencies of encrypted message
	pseudoFreq = calculateLetterFrequencies(message)

	diffArray = Array.new
	rotated = Array.new
	rotated.replace(pseudoFreq)
	for i in (0..realFreq.length) do
		#Step 2: check difference with ideal letter frequency distribution
		diffArray << checkDiff(realFreq, rotated)
		#Step 3: rotate pseudoFreq by 1 position
		rotated = rotated.rotate
	end
	#Step 5: find the array with the smallest difference
	rot = diffArray.index(diffArray.min)
	#puts(diffArray)
	return codeMessage("decode", rot, message)
end

def calculateLetterFrequencies(message)
	freq = Array.new
	uMessage = message.upcase()
	noSpace = message.split.join()
	i = 65
	while i < 91 do
		c = i.chr
		count = 0
		noSpace.split('').each do |n|
			if n == c
				count+=1
			end
		end
		freq << (count.to_f/noSpace.length)*100
		i+=1
	end
	return freq
end

def checkDiff(real, pseudo)
	#Step 1: calculate the differences for each value of the array
	diffs = Array.new
	for i in 0..(real.length-1)
		diffs << (real[i] - pseudo[i])
	end
	#Step 2: raise each difference to the power of 2
	diffSquared = Array.new
	for x in 0..(diffs.length-1)
		diffSquared << (diffs[x]**2)
	end
	#Step 3: return the average of the differences
	return rms(diffSquared)
end

def rms(seq)
  return Math.sqrt(seq.inject(0.0) {|sum, x| sum + x*x} / seq.length)
end

#DISPLAYING X GUESSES
def getBestGuesses(x, diffArray)
	guesses = Array.new
	for i in 0..x
		minDex = diffArray.index(diffArray.min)
		guesses << minDex
		diffArray[minDex] = diffArray.max
	end
	return guesses
end

def main()
	if ARGV.length > 1
		command = ARGV[0]
		if command == "crack"
			messages = ARGV[1..ARGV.length-1]
			messages.each do |m|
				puts(crack(m))
			end
			#puts("Cracking Caesar Cipher coming soon!")
		elsif (command == "encode" or command == "decode") and ARGV.length > 2
			rot = ARGV[1]
			mess = ARGV[2..ARGV.length-1]
			mess.each do |m|
				puts(codeMessage(command, rot, m))
			end
		else
			puts("args don't match the command you entered")
		end
	else
		puts("Not enough arguments")
	end
end

main()