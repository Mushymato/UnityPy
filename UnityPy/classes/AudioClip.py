from .NamedObject import NamedObject
from ..ResourceReader import ResourceReader

from ..enums import AudioType, AudioCompressionFormat, AUDIO_TYPE_EXTEMSION
from ..export import AudioClipConverter


class AudioClip(NamedObject):
	def __init__(self, reader):
		super().__init__(reader=reader)
		version = self.version
		if version[0] < 5:  #
			self.m_Format = reader.read_int()
			self.m_Type = AudioType(reader.read_int())
			self.m_3D = reader.read_boolean()
			self.m_UseHardware = reader.read_boolean()
			reader.align_stream()

			if version[0] >= 4 or (version[0] == 3 and version[1] >= 2):  # 3.2.0 to 5
				self.m_Stream = reader.read_int()
				m_Size = reader.read_int()
				tsize = m_Size + 4 - m_Size % 4 if (m_Size % 4 != 0) else m_Size
				if reader.byte_size + reader.byte_start - reader.Position != tsize:
					m_Offset = reader.read_int()
					self.m_Source = self.assets_file.full_name + ".resS"
			else:
				m_Size = reader.read_int()

			self.extension = AUDIO_TYPE_EXTEMSION.get(self.m_Type, '.audioclip')
		else:
			self.m_LoadType = reader.read_int()
			self.m_Channels = reader.read_int()
			self.m_Frequency = reader.read_int()
			self.m_BitsPerSample = reader.read_int()
			self.m_Length = reader.read_float()
			self.m_IsTrackerFormat = reader.read_boolean()
			reader.align_stream()
			self.m_SubsoundIndex = reader.read_int()
			self.m_PreloadAudioData = reader.read_boolean()
			self.m_LoadInBackground = reader.read_boolean()
			self.m_Legacy3D = reader.read_boolean()
			reader.align_stream()
			self.m_Source = reader.read_aligned_string()
			m_Offset = reader.read_long()
			m_Size = reader.read_long()
			self.m_CompressionFormat = AudioCompressionFormat(reader.read_int())

			self.extension = AUDIO_TYPE_EXTEMSION.get(self.m_CompressionFormat, '.audioclip')

		if self.m_Source:
			resourceReader = ResourceReader(self.m_Source, self.assets_file, m_Offset, m_Size)
		else:
			resourceReader = ResourceReader(reader, reader.Position, m_Size)
		self.m_AudioData = resourceReader.get_data()

	@property
	def samples(self) -> dict:
		return AudioClipConverter.extract_audioclip_samples(self)
