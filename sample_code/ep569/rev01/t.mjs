import unzipper from 'unzipper';

const archive = await unzipper.Open.file(process.argv[2]);
await archive.extract({path: process.argv[3], concurrent: 2});
